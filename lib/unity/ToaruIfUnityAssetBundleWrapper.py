import UnityPy
from lib.unity.UnityAssetBundleWrapper import UnityAssetBundleWrapper

class ToaruIfUnityAssetBundleWrapper(UnityAssetBundleWrapper):

    def __init__(self, destinationPath: str, debugMode: bool = False):
        super().__init__(destinationPath=destinationPath, debugMode=debugMode)
    
    # SAMPLE
    def filterTexture2D(self, obj):
        return self.__extractImage(obj)