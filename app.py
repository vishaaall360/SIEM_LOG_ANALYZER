from flask import Flask, render_template
from log_parser import parse_logs
from detection_rules import detect_bruteforce
from alert_engine import generate_alerts

app = Flask(__name__)

@app.route("/")
def dashboard():
    logs = parse_logs("logs/auth.log")
    alerts = detect_bruteforce(logs)
    alerts = generate_alerts(alerts)

    return render_template(
        "dashboard.html",
        logs=logs,
        alerts=alerts
    )

if __name__ == "__main__":
    app.run(debug=True)
