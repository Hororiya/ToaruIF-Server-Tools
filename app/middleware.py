from flask import request, jsonify
from functools import wraps
from ..lib.toaruIF.seaes import encrypt, decrypt
from .config import Config

def encrypted_route(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Decrypt the incoming request if it has encrypted data
        if request.is_json and 'data' in request.json and Config.IS_CRYPT == 1:
            encrypted_data = request.json.get('data')
            try:
                # Decrypt the incoming request data
                decrypted_data = decrypt(encrypted_data)
                request.json.update(eval(decrypted_data))  # Convert decrypted string to dictionary
            except Exception as e:
                return jsonify({"error": "Decryption failed", "message": str(e)}), 400
        
        # Call the actual route function
        response = f(*args, **kwargs)

        # Encrypt the outgoing response
        if response.is_json and Config.IS_CRYPT == 1:
            response_data = response.get_json()
            encrypted_response = encrypt(str(response_data))
            return encrypted_response, response.status_code

        return response
    return decorated_function