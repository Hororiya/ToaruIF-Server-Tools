from app import create_app

app = create_app()

if __name__ == '__main__':
    # Specify the certificate and key files for HTTPS
    app.run(ssl_context=('certs/server.crt', 'certs/server.key'), host='0.0.0.0', port=40443)