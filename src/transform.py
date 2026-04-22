import pandas as pd

def transform_data(df):
    #calc expected journey duration (mins)
    df["expected_duration"] = (df["arrival_time"] - df["departure_time"]).dt.total_seconds() / 60

    #calc actual journey duration
    df["actual_duration"] = (df["actual_arrival_time"] - df["departure_time"]).dt.total_seconds() / 60

    #calc delay
    df["delay_minutes"] = df["actual_duration"] - df["expected_duration"]

    #classify delays
    def classify_delay(x):
        if x > 30:
            return "Critical"
        elif x > 10:
            return "Moderate"
        elif x > 0:
            return "Minor"
        else:
            return "On Time"
        
    df["delay_status"] = df["delay_minutes"].apply(classify_delay)

    #extract time features
    df["hour"] = df["departure_time"].dt.hour
    df["day"] = df["departure_time"].dt.day_name()

    return df