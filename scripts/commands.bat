docker build -t avigoldshtein/crud-app-with-mongo .
docker push avigoldshtein/crud-app-with-mongo:latest

cd ..\infrastructure\k8s
oc apply -f .\mongo-crud-secret.yaml
oc apply -f .\mongoDB-pvc.yaml
oc apply -f .\mongoDB-deployment.yaml
oc apply -f .\mongoDB-svc.yaml
oc apply -f .\crud-app-deployment.yaml
oc apply -f .\crud-app-svc.yaml
oc apply -f .\crud-app-route.yaml

set POD_NAME=mongodb-deployment-5b8fcc9df5-gjhbg

oc cp .\create-insert-data.sh %POD_NAME%:/tmp/create-insert-data.sh

oc exec -i %POD_NAME% -- /bin/bash -c "mongosh -u root -p pass --authenticationDatabase admin enemy_soldiers --file './tmp/create-insert-data.sh'"


set POD_NAME=mongodb-deployment-5b8fcc9df5-gjhbg
oc rsh %POD_NAME% 
mongosh -u root -p pass --authenticationDatabase admin enemy_soldiers
db.createCollection("soldier_details")