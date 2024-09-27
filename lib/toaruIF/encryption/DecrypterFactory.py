import os
import struct
from lib.toaruIF.utils.BinaryReader import BinaryReader, SeekOrigin
from lib.toaruIF.encryption.OffsetDecrypter import OffsetDecrypter
from lib.toaruIF.encryption.XorDecrypter import XorDecrypter

class DecrypterFactory:

    Keys = {}

    def __init__(self, keysFilePath: str) -> None:
        
        if not os.path.exists(keysFilePath):
            raise FileNotFoundError(f"key file {keysFilePath} not found")

        keysFileContent = open(keysFilePath, "rb")

        self.LoadKeys(keysFileContent)
        pass

    def LoadKeys(self, keysFileContent: bytes) -> None:
        br = BinaryReader(keysFileContent)

        br.Seek(0, SeekOrigin.Begin)
        len = br.ReadInt32()
        i = 0
        while (i < len):
            key_sig = br.ReadInt32()
            key_len = br.ReadInt32()
            key = br.Read(key_len)
            self.Keys[key_sig] = key
            i += 1
        pass

    def GetDecrypter(self, blob):
        buff = bytearray(4)
        br = BinaryReader(blob=blob)
        br.Seek(0x07, SeekOrigin.Begin)
        buff = br.Read(buff.__len__())

        # XorDecrypter scenario 1
        if (buff[0] == buff[1] and buff[0] == buff[2] and buff[0] == buff[3]):
            return XorDecrypter(buff)
        # OffsetDecrypter scenario
        if (buff[0] == 0x53 and buff[1] == 0x00 and buff[2] == 0x00 and buff[3] == 0x00):
            buff = bytearray(7)
            while (br.GetPosition() + 7 < br.GetLength()):
                buff = br.Read(7)
                br.Seek(1 - buff.__len__(), SeekOrigin.Current)
                try:
                    if (buff.decode("ascii") == "UnityFS"):
                        return OffsetDecrypter(br.GetPosition() - 1)
                except:
                    pass
            return None

        # XorDecrypter scenario 2
        buff_int = struct.unpack_from("=i", buff, offset=0)[0]
        if (self.Keys.get(buff_int)):
            return XorDecrypter(self.Keys[buff_int])

        return None