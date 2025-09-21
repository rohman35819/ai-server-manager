# ai-server-manager
Script Python untuk mengatur server AI dengan OpenAI API + worker manager


🔍 Penjelasan Per Modul
Folder	Fungsi
app/	Semua logic utama sistem
routes/	REST API endpoints
services/	Backend logic seperti monitoring, prediksi AI, logging
models/	Model machine learning & schema input/output API
utils/	Tools tambahan (scheduling, alerting, dsb)
scripts/	Script mandiri untuk training model, simulasi, monitoring
data/	Data mentah (log & metrik)
tests/	Unit & integration tests
.env	Token API, DB URL, setting lainnya
Dockerfile	Untuk containerisasi aplikasi
docker-compose.yml	Integrasi semua service (API, worker, DB, monitoring stack)

🚀 Tools/Stack yang Digunakan
Fungsi	Tools
API backend	FastAPI / Flask
ML/AI Engine	Scikit-learn / PyTorch
Monitoring server	psutil, Prometheus
Log & Metric storage	Elasticsearch, TimescaleDB
Scheduler	Celery + Redis
Dashboard (opsional)	Grafana/Kibana
Containerization	Docker + Docker Compose
Alerts (opsional)	Telegram/Slack Webhook




# AI Server Manager

Sistem AI untuk monitoring, deteksi anomali, dan pengelolaan server berbasis FastAPI.

## Fitur
- Monitoring CPU, RAM, Disk
- Deteksi anomali berbasis Machine Learning
- API endpoint dengan FastAPI
- Logging sederhana
- Bisa dijalankan via Docker

## Menjalankan

```bash
docker-compose up --build
