# 🛡️ SIEM Log Analyzer & Threat Detection System

The SIEM Log Analyzer & Threat Detection System is a cyber-security project that simulates the core functionality of a Security Information and Event Management (SIEM) platform. It analyzes system authentication logs to detect suspicious activities such as brute-force login attempts and generates security alerts, similar to real-world SOC monitoring tools.

This project is designed to demonstrate blue-team cyber security skills and is suitable for academic use as well as a strong GitHub portfolio project.

---

## 🚀 Features

- Analyzes system authentication logs
- Detects brute-force login attacks
- Identifies suspicious IP behavior
- Generates real-time security alerts
- Displays logs and alerts in a web dashboard
- Simple and modular architecture

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – Web framework
- **HTML & CSS** – Frontend
- **Rule-based detection logic**

---

## 📁 Project Structure

siem-log-analyzer/
│
├── app.py
├── log_parser.py
├── detection_rules.py
├── alert_engine.py
├── requirements.txt
│
├── logs/
│ └── auth.log
│
├── templates/
│ └── dashboard.html
│
├── static/
│ └── style.css

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

pip install flask

2️⃣ Run the Application

python app.py

3️⃣ Open in Browser

http://127.0.0.1:5000

🧪 Sample Detection Scenario
| Log Event                           | Result                      |
| ----------------------------------- | --------------------------- |
| Multiple failed logins from same IP | Brute-force attack detected |
| Successful login after failures     | Logged as normal activity   |

👨‍💻 Author

Vishaal S
GitHub: https://github.com/vishaal360
