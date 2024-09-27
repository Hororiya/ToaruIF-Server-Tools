# Create the certs directory
mkdir certs

# Generate the private key and certificate
openssl req -newkey rsa:2048 -nodes -keyout certs/server.key -x509 -days 365 -out certs/server.crt