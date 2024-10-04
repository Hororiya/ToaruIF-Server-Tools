import os
import base64

def generateBytes(bytesSize: int = 16):
    # Generate 16 random bytes (or however many you need)
    random_bytes = os.urandom(bytesSize)

    # Base64 encode the random bytes
    encoded_bytes = base64.b64encode(random_bytes)

    # Convert to string for easy display (optional)
    return encoded_bytes.decode("utf-8")