docker build -t avigoldshtein/crud-app-with-mongo:latest .
docker push avigoldshtein/crud-app-with-mongo:latest

oc apply -f ..\infrastructure\k8s\mongoDB-secret.yaml
oc apply -f ..\infrastructure\k8s\mongoDB-pvc.yaml
oc apply -f ..\infrastructure\k8s\mongoDB-deployment.yaml
oc apply -f ..\infrastructure\k8s\mongoDB-svc.yaml
oc apply -f ..\infrastructure\k8s\crud-app-secret.yaml
oc apply -f ..\infrastructure\k8s\crud-app-deployment.yaml
oc apply -f ..\infrastructure\k8s\crud-app-svc.yaml

oc expose svc/mongodb-crud-svc