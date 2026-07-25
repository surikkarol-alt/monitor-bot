# MonitorBOT

Dockerized log monitoring system with Telegram alerts.

## 📌 Overview

MonitorBOT is a container-based log monitoring service built with Python and Docker.  
It monitors application logs, detects issues, and sends real-time alerts to Telegram.

The project demonstrates practical DevOps skills including containerization, CI/CD, and Linux service deployment.

---

## ⚙️ Features

- Log monitoring and parsing
- Telegram bot integration for alerts
- Docker & Docker Compose deployment
- Environment variable configuration
- CI/CD with GitHub Actions
- Linux systemd service integration

---

## 🛠 Technologies

- Python
- Docker
- Docker Compose
- Linux
- GitHub Actions
- Telegram Bot API

---

## 🚀 How to Run

1. Clone the repository:

`bash
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME

# 🚨 Monitor Bot (Dockerized Log Monitoring Service)

This project is a **Docker-based Python monitoring service** that watches a log file in real time and sends alerts to Telegram when `ERROR` or `CRITICAL` messages appear.

The service is designed following **DevOps best practices**:
- runs as a Docker container
- uses environment variables for configuration
- supports health checks
- persists logs via Docker volumes

---

## 🧩 Architecture Overview

- **Python service** (`monitor.py`)  
  Watches a log file and reacts to new lines.
- **Telegram integration**  
  Sends alerts using Telegram Bot API.
- **Docker container**  
  Runs the service in an isolated environment.
- **Docker Compose**  
  Used to configure and run the service.
- **Healthcheck**  
  Docker verifies that the service is alive and working.

---

## 📁 Project Structure

```text
monitor_bot/
├── app/
│   ├── main.py              # Entry point
│   ├── monitor.py           # Log monitoring logic
│   ├── telegram_sender.py   # Telegram API client
│   ├── config.py            # Environment variables
│   └── logs/                # Log files (Docker volume)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

