import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    #convert datetime cols
    df["date_of_journey"] = pd.to_datetime(df["date_of_journey"], errors="coerce")
    df["departure_time"] = pd.to_datetime(df["departure_time"], errors="coerce")
    df["arrival_time"] = pd.to_datetime(df["arrival_time"], errors="coerce")
    df["actual_arrival_time"] = pd.to_datetime(df["actual_arrival_time"], errors="coerce")

    #drop rows missing key fields
    df = df.dropna(subset=[
        "departure_time",
        "arrival_time",
        "actual_arrival_time"
    ])

    return df


