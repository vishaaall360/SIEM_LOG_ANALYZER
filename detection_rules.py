from collections import defaultdict

def detect_bruteforce(logs, threshold=3):
    failed_attempts = defaultdict(int)
    alerts = []

    for log in logs:
        if "Failed password" in log:
            ip = log.split()[-1]
            failed_attempts[ip] += 1

            if failed_attempts[ip] == threshold:
                alerts.append(f"Brute Force Attack Detected from IP: {ip}")

    return alerts
