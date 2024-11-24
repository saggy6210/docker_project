# For info-app
Very simple info world python Flask application.
python -m venv .venv
. .venv/bin/activate
pip install flask==3.0.3
pip install redis==5.2.0

# For info-app

#Docker commands:

1. To get a list of docker images
docker images 

2. To build the docker image 
docker build -f Dockerfile -t info-app:latest .

3. Run a docker image or create a container 
docker run -p 5001:5000 info-app

4. Verify the application is working with docker
http://127.0.0.1:5001 

* Kubernetes commands: *
1. Set configuration file
export KUBECONFIG=~/.kube/config

2. Get running nodes in the Kubernetes cluster
kubectl get nodes

3. Get the list of running pods in the Kubernetes cluster
kubectl get pods

4. Deploy the application using .yml file
kubectl apply -f deployment.yaml

kubectl expose deployment info-app --type="LoadBalancer“ -> if deployment won’t work

5. Get the list of services 
kubectl get svc

6. Delete the deployment 
kubectl delete deployment info-app

7. Delete service 
kubectl delete svc info-app-service


