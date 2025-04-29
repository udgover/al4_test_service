docker build --no-cache -t testing/assemblyline-service-test . 
docker tag testing/assemblyline-service-test localhost:32000/testing/assemblyline-service-test 
docker push --all-tags localhost:32000/testing/assemblyline-service-test