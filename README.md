# K8S
This repository Includes a flask application, and using redis for caching. Deployed in a kubernetes cluster as a sidecar to the flask app.
2 replicas deployed, and hosted through service controller (NodePort). Really nice example for load balancing. You can visually see which instance / replica you are getting, by the counter displayed on the screen 

how to run :

k3d cluster create flask-cluster -p "8080:30080@loadbalancer"

kubectl apply -f flask-redis-deployment.yml

kubectl apply -f flask-redis-service.yml


check localhost:8080 


when done playing dont forget to :

k3d cluster delete flask-cluster


