def calculate_metrics(df):
    total_journeys = len(df)

    delay_rate = (df["delay_status"] != "On Time").mean()

    avg_delay = df["delay_minutes"].mean()

    top_delay_reasons = df["reason_for_delay"].value_counts().head(5)

    worst_routes = (
        df.groupby(["departure_station", "arrival_destination"])["delay_minutes"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    return {
        "total_journeys": total_journeys,
        "delay_rate": delay_rate,
        "avg_delay": avg_delay,
        "top_delay_reasons": top_delay_reasons,
        "worst_routes": worst_routes
    }