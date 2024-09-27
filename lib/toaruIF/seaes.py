from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import secrets


def encrypt(message, key, iv=None):
    msg_length = len(message)
    encrypted_length = msg_length + 16
    aes = AES.new(key, AES.MODE_ECB)
    encrypted = bytearray(encrypted_length)
    if iv is not None:
        encrypted[:16] = iv[:16]
    else:
        encrypted[:16] = secrets.token_bytes(16)
    xor_block = encrypted[:16]
    enc_data = bytearray(msg_length)

    offset = 0
    remaining = msg_length

    if msg_length < 16:
        iv = encrypted[:msg_length]
        plain=bytearray(16)
        plain[:msg_length] = strxor(message, iv)
        plain[msg_length:] = encrypted[msg_length:16]
        temp_block = aes.encrypt(plain)
        encrypted[msg_length:] = temp_block[:]
        return encrypted

    while remaining > 32 or (len(message)%16==0 and remaining > 0):
        plain_block = message[offset:offset + 16]
        for j in range(16):
            plain_block[j] = plain_block[j] ^ xor_block[j]
        enc_block = aes.encrypt(plain_block)
        enc_data[offset:offset+16] = enc_block
        xor_block = enc_block
        remaining -= 16
        offset += 16
    if remaining == 0 :
        encrypted[16:] = enc_data
        return encrypted
    plain_block = message[offset:offset + 16]
    for j in range(16):
        plain_block[j] = plain_block[j] ^ xor_block[j]
    last_enc_block = bytearray(16)
    last_enc_block[:16] = aes.encrypt(plain_block)
    remaining -= 16
    enc_data[offset + 16:] = last_enc_block[:remaining]
    for i in range(remaining):
        last_enc_block[i] = last_enc_block[i] ^ message[offset + i + 16]
    enc_data[offset:offset+16] = aes.encrypt(last_enc_block)
    encrypted[16:] = enc_data
    return encrypted

def decrypt(message, key):
    actual_encrypted_length = len(message) - 16

    aes = AES.new(key, AES.MODE_ECB)
    decrypted = bytearray(actual_encrypted_length)

    xor_block = message[:16]
    data = message[16:]

    offset = 0
    remaining = actual_encrypted_length

    if len(message) < 32:
        iv = message[:actual_encrypted_length]
        enc = message[actual_encrypted_length:]
        temp_block = aes.decrypt(enc)
        decrypted[:len(iv)] = strxor(temp_block[:actual_encrypted_length], iv)
        return decrypted

    while remaining > 32 or (len(message)%16==0 and remaining > 0):
        enc_block = data[offset:offset + 16]
        dec_block = aes.decrypt(enc_block)
        for j in range(16):
            decrypted[offset + j] = dec_block[j] ^ xor_block[j]
        xor_block = enc_block
        remaining -= 16
        offset += 16
    if remaining == 0 :
        return decrypted
    dec_block = aes.decrypt(data[offset:offset + 16])
    remaining -= 16
    for i in range(remaining):
        decrypted[offset + i + 16] = dec_block[i] ^ data[offset + i + 16]

    last_enc_block = bytearray(16)
    for i in range(16):
        if i < remaining:
            last_enc_block[i] = data[offset + i + 16]
        else:
            last_enc_block[i] = dec_block[i]

    dec_block = aes.decrypt(last_enc_block)
    for j in range(16):
        decrypted[offset + j] = dec_block[j] ^ xor_block[j]

    return decrypted

if __name__ == '__main__':
    message = bytearray(
        b'{"res_code":0,"res_str":"OK","server_time":1696597142,"session_time":1696598938,"patch_version":130573,"tag_schedule_version":11350}\n{"hand_shake":{"userid":2717890},"do_create_user":0,"tutorial_download_idx":1,"inviteid":166686349}')
    key = bytearray(b'nqnfAHZEOrkyl5SU6HXWPoMebHyTdqKN')
    enc = encrypt(message, key)
    # print(''.join(['{:02x}'.format(byte) for byte in enc]))
    decrypted_message = decrypt(enc, key)
    print(decrypted_message)
