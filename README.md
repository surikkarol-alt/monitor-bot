# 🚀 MonitorBot

MonitorBot is a Python application for monitoring Docker containers and sending real-time Telegram notifications.

The project demonstrates practical DevOps skills, including Docker, Docker Compose, CI/CD with GitHub Actions, automated testing, and Linux deployment.

---

# ✨ Features

- 📦 Docker container monitoring
- 📲 Telegram alerts
- 🔄 Automatic restart support
- ❤️ Health checks
- 🧪 Pytest tests
- ✔️ Flake8 code quality checks
- 🚀 GitHub Actions CI/CD
- 🔐 Environment variables (.env)

---

# 🛠 Tech Stack

- Python 3.11
- Docker
- Docker Compose
- Git
- GitHub
- GitHub Actions
- Linux
- Telegram Bot API

---

# 📁 Project Structure

```text
monitor_bot/
├── app/
│   ├── main.py
│   ├── monitor.py
│   ├── telegram.py
│   ├── config.py
│   ├── logger.py
│   ├── health.py
│   └── ...
├── tests/
├── .github/
│   └── workflows/
├── Dockerfile
├── Dockerfile.test
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/surikkarol-alt/monitor-bot.git
cd monitor-bot
```

Create the environment file:

```bash
cp .env.example .env
```

Build the Docker image:

```bash
docker compose build
```

Start the project:

```bash
docker compose up -d
```

---

# 🧪 Run Tests

```bash
pytest
```

---

# ✔️ Code Quality

```bash
flake8 .
```

---

# 🐳 Docker

Build image:

```bash
docker build -t monitorbot .
```

Run container:

```bash
docker run monitorbot
```

---

# 🔄 Continuous Integration

Every push to GitHub automatically:

- runs Flake8
- runs Pytest
- builds the Docker image

GitHub Actions ensures that the project remains in a working state.

---

# 🎯 Future Improvements

- Web dashboard
- Email notifications
- Prometheus metrics
- Grafana dashboards
- Kubernetes deployment

---

# 👨‍💻 Author

Created as a learning and portfolio project while studying Python, Linux, Docker, and DevOps.

GitHub:
https://github.com/surikkarol-alt
