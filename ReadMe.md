# 1.	Deploying the ConfigMap and Secret:
kubectl apply -f backend-configmap.yaml
kubectl apply -f database-configmap.yaml

# 2.   Deploying the App
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml
kubectl apply -f database-deployment.yaml
kubectl apply -f database-service.yaml


# Building the container image
Docker-compose build


# Starting the Cluster
minikube start

# Retreiving nodes information
kubectl get nodes

# retreiving services information
 kubectl get svc
