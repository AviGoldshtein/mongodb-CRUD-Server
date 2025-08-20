docker build -t avigoldshtein/crud-app-with-mongo:latest .
docker push avigoldshtein/crud-app-with-mongo:latest

cd ..\infrastructure\k8s
oc apply -f .\mongo-crud-secret.yaml
oc apply -f .\mongoDB-pvc.yaml
oc apply -f .\mongoDB-deployment.yaml
oc apply -f .\mongoDB-svc.yaml
oc apply -f .\crud-app-deployment.yaml
oc apply -f .\crud-app-svc.yaml

oc expose svc/mongodb-crud-svc