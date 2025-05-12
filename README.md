# K8S
simple repo. Including a flask application, and using redis for caching. Deployed in a kubernetes cluster as a sidecar to the flask app.

how to run :

k3d cluster create flask-cluster -p "8080:30080@loadbalancer"

kubectl apply -f flask-redis-deployment.yml

kubectl apply -f flask-redis-service.yml


check localhost:8080 


when done playing dont forget to :

k3d cluster delete flask-cluster


