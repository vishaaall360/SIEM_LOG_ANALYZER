def generate_alerts(alerts):
    formatted = []
    for alert in alerts:
        formatted.append({
            "type": "Security Alert",
            "message": alert
        })
    return formatted
