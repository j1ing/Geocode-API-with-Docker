# 🐳Dockerized Geocode API

A simple geocoding client-server application built with FastAPI and Python, containerized using Docker and Docker Compose.

## 🚀Features

- FastAPI server exposes a `/geocode` endpoint that accepts an address and returns latitude and longitude.
- Client program allows you to input addresses from the command line and fetch coordinates.
- Dockerized architecture with separate client and server containers.
- Docker Compose manages multi-container setup and handles service dependencies with health checks.

## Getting Started

### ✅Prerequisites

- Docker Desktop installed and running (https://www.docker.com/products/docker-desktop)
- Docker Compose (comes with Docker Desktop)
- (Optional) Docker Extension for VSCode

### 🛠️Setup and Run

1. Create an .env file in client/ folder and in server/ folder

For client/.env:
<pre><code>
API_GEOCODE = http://server:8000/geocode
</code></pre>
For server/.env:
<pre><code>
URL_MAP = https://nominatim.openstreetmap.org/search
USER_EMAIL = youremail@email.com
</code></pre>

2. Build and run server container in detached mode on cmd
<pre><code>
docker compose up -d server
</code></pre>

3. Build and run client container on cmd
<pre><code>
docker compose run --rm client
</code></pre>

4. Exit the application by entering Quit when prompted.

5. To clean up docker images and containers from this docker compose
<pre><code>
docker compose down --rmi all
</code></pre>


### 📦Project Structure
<pre><code>
├── client/                # CLI client app
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt   # Client-side python setup
├── server/                # FastAPI server
│   ├── Dockerfile
│   ├── server.py
│   └── requirements.txt   # Server-side python setup
├── docker-compose.yml     # Multi-container orchestration
├── .gitignore
└── README.md
</code></pre>


### 📝Notes
Environment variables are loaded separately for client and server.

Server includes a healthcheck endpoint (/docs) to coordinate startup timing.

curl is used in the server container to support health checks.