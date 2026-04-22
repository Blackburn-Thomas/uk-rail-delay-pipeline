from src.ingest import load_data
from src.clean import clean_data
from src.transform import transform_data
from src.storage import save_to_db
from src.metrics import calculate_metrics
from src.alerts import check_alerts

def run_pipeline():
    df = load_data()
    df = clean_data(df)
    df = transform_data(df)

    #save processed data
    df.to_csv("data/processed/processed_data.csv", index=False)

    save_to_db(df)

    metrics = calculate_metrics(df)
    alerts = check_alerts(metrics)

    print("\n---METRICS---")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    print("\n---ALERTS---")
    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    run_pipeline()