from lib.toaruIF.utils.BinaryReader import BinaryReader, SeekOrigin

class XorDecrypter:

    Key = b''

    def __init__(self, key: bytes = b'') -> None:
        self.Key = key
        pass

    def Decrypt(self, input: BinaryReader) -> BinaryReader:
        input.Seek(0, SeekOrigin.Begin)

        len = self.Key.__len__()
        ptr = len - 7

        buffer = bytearray(input.GetBlob())
        i = 0

        while (i < buffer.__len__()):
            buffer[i] = buffer[i] ^ self.Key[ptr]
            ptr += 1
            if (ptr == len):
                ptr = 0
            i += 1

        return BinaryReader(buffer)
