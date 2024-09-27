from lib.toaruIF.utils.BinaryReader import BinaryReader

class IDecrypter:
    def Decrypt(input: BinaryReader) -> BinaryReader:
        raise NotImplementedError("abstract class")
