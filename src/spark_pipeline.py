from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, avg, count
from pyspark.sql.types import TimestampType

def run_spark_pipeline(file_path="data/raw/train_data.csv"):
    #start spark session
    spark = SparkSession.builder \
        .appName("UKRailSparkPipeline") \
        .getOrCreate()
    
    #load data
    df = spark.read.csv(file_path, header=True, inferSchema=True, sep=";")

    #standardise column names
    df = df.toDF(*[
        c.strip().lower().replace(" ", "_")
        for c in df.columns
    ])

    #convert time columns
    df = df.withColumn("arrival_time", col("arrival_time").cast(TimestampType()))
    df = df.withColumn("actual_arrival_time", col("actual_arrival_time").cast(TimestampType()))

    #drop nulls
    df = df.dropna(subset=["arrival_time", "actual_arrival_time"])

    #calculate delay in minutes
    df = df.withColumn(
        "delay_minutes",
        (col("actual_arrival_time").cast("long") - col("arrival_time").cast("long")) / 60
    )

    #catergorise delays
    df = df.withColumn(
        "delay_category",
        when(col("delay_minutes") <= 0, "On Time")
        .when(col("delay_minutes") < 10, "Minor")
        .when(col("delay_minutes") < 30, "Moderate")
        .otherwise("Critical")
    )

    #example aggregations
    print("\n=== Delay Category Counts ===")
    df.groupBy("delay_category").count().show()

    print("\n=== Average Delay ===")
    df.select(avg("delay_minutes")).show()

    print("\n=== Worst Routes ===")
    df.groupBy("departure_station", "arrival_destination") \
        .agg(avg("delay_minutes").alias("avg_delay"), count("*").alias("journeys")) \
        .orderBy(col("avg_delay").desc()) \
        .show(10)

    spark.stop()

if __name__ == "__main__":
    run_spark_pipeline()