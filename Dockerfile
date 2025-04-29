FROM cccs/assemblyline-v4-service-base:stable

# Python path to the service class from your service directory
ENV SERVICE_PATH=test.TestAL4

# Copy service code
WORKDIR /opt/al_service
COPY . .
