import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/train_data.csv", sep=";")
    print(f"Loaded {len(df)} rows")
    return df
