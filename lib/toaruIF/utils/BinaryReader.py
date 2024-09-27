from io import BufferedReader
import struct

class SeekOrigin:
    Begin = 0
    Current = 1
    End = 2

class BinaryReader:
    blob = b''
    index = 0

    def __init__(self, blob: bytes = b'') -> None:

        if (isinstance(blob, BufferedReader)):
            blob = blob.read()

        self.blob = blob
        pass

    def GetPosition(self) -> int:
        return self.index

    def GetLength(self) -> int:
        return self.blob.__len__()

    def GetBlob(self) -> bytes:
        return self.blob

    def SetBlob(self, blob: bytes):
        self.blob = blob
        pass

    def Seek(self, index: int, mode: SeekOrigin):

        if (mode == SeekOrigin.Begin):
            self.index = index
        elif (mode == SeekOrigin.Current):
            self.index += index
        elif (mode == SeekOrigin.End):
            self.index = self.GetLength() - index

        pass

    def Read(self, bytesToRead: int):
        if (self.index+bytesToRead > self.GetLength()):
            raise EOFError()
        data = self.blob[self.index:self.index+bytesToRead]
        self.index += bytesToRead
        return data
    
    def ReadUntilEof(self) -> bytes:
        return self.Read(self.GetLength() - self.GetPosition())

    def ReadInt32(self):
        data = self.Read(4)
        return struct.unpack("=i", data)[0]