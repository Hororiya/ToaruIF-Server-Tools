from lib.toaruIF.utils.BinaryReader import BinaryReader, SeekOrigin

class OffsetDecrypter:

    Offset = 0

    def __init__(self, offset = 0) -> None:
        self.Offset = offset
        pass

    def Decrypt(self, input: BinaryReader) -> BinaryReader:
        input.Seek(self.Offset, SeekOrigin.Begin)
        return BinaryReader(input.ReadUntilEof())
