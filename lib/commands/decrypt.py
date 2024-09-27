import os
from lib.toaruIF.encryption.DecrypterFactory import DecrypterFactory
from lib.toaruIF.utils.BinaryReader import BinaryReader

def decrypt(input: bytes, outputPath: str, keysFilePath: str):
    keysFactory = DecrypterFactory(keysFilePath=keysFilePath)

    decryptor = keysFactory.GetDecrypter(input)
    if (decryptor is None):
        raise ModuleNotFoundError("decryption method not implemented")
    open(outputPath, "wb").write(decryptor.Decrypt(input=BinaryReader(input)).GetBlob())

def decryptBlob(input: bytes, keysFilePath: str):
    keysFactory = DecrypterFactory(keysFilePath=keysFilePath)

    decryptor = keysFactory.GetDecrypter(input)
    if (decryptor is None):
        raise ModuleNotFoundError("decryption method not implemented")
    return decryptor.Decrypt(input=BinaryReader(input)).GetBlob()