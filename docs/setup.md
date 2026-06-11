# Kubernetes Observability Setup

## Components

- Deployment
- Service
- ConfigMap
- Prometheus
- Grafana

## Local Setup

1. Install Minikube
2. Start cluster

kubectl apply -f manifests/

3. Deploy monitoring stack

kubectl apply -f monitoring/
