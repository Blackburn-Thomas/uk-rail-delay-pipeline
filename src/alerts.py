def check_alerts(metrics):
    alerts = []

    if metrics["delay_rate"] > 0.25:
        alerts.append("⚠️ High delay rate across network")

    if metrics["avg_delay"] > 15:
        alerts.append("⚠️ Average delays exceeding threshold")

    return alerts

