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

@REM set POD_NAME=python-app-crud-mongo-6d7479b994-2jf8s

@REM oc cp .\create-insert-data.sh %POD_NAME%:/tmp/create-insert-data.sh

@REM oc exec -i %POD_NAME% -- /bin/bash -c "mongosh -u root -p pass --authenticationDatabase admin enemy_soldiers --file './tmp/create-insert-data.sh'"


@REM set POD_NAME=python-app-crud-mongo-6d7479b994-2jf8s
@REM oc rsh %POD_NAME% 
@REM mongosh -u root -p pass --authenticationDatabase admin enemy_soldiers
@REM db.createCollection("soldier_details")