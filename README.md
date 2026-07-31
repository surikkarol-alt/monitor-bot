# MonitorBot

MonitorBot is a Python-based monitoring system that checks the availability of a web service and sends Telegram notifications when the service goes DOWN or RECOVERS.

## Features

- Service health monitoring
- Telegram notifications
- Docker / Podman support
- GitHub Actions CI
- Automatic deployment to Oracle Cloud VPS
- Flask test service
- Logging
- Environment configuration with .env

## Project Structure

```
app/
tests/
Dockerfile
docker-compose.yml
README.md
```

## Technologies

- Python 3.11
- Flask
- Requests
- Podman
- Docker Compose
- GitHub Actions
- Oracle Cloud VPS
- Linux
- Git

## CI/CD

Every push to the `main` branch:

1. Runs flake8
2. Runs pytest
3. Builds the container
4. Publishes the image
5. Deploys automatically to Oracle Cloud VPS

## Telegram Alerts

Example:

```
test-service is DOWN
test-service RECOVERED
```

## Author

Sharif
