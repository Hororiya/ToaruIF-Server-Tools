import os
import json
import UnityPy
from lib.unity.UnityAssetType import UnityAssetType
from lib.unity.MonoBehaviourJsonEncoder import MonoBehaviourJsonEncoder

class UnityAssetBundleWrapper:

    def __init__(self, destinationPath: str, debugMode: bool = False):
        self.destinationPath = destinationPath
        self.tempBundlePath = None
        self.debugMode = debugMode

    def extractBundle(self, pathOrBlobBytes: bytes, pathOutput: str = None) -> list:
        assetFiles = []

        # bundleName temp
        if not pathOutput is None:
            self.tempBundlePath = pathOutput
        elif type(pathOrBlobBytes) is str:
            self.tempBundlePath = pathOrBlobBytes
        else:
            self.tempBundlePath = None
        
        bundle = UnityPy.load(pathOrBlobBytes)
        iterator = bundle.objects
        for obj in iterator:
            _type = str(obj.type)
            
            try:
                _name = obj.read().name
            except TypeError:
                if self.debugMode:
                    print("DEBUG", _type, "unknown")
                    continue
            except AttributeError:
                _name = "Error on getting name"
                if self.debugMode:
                    print("DEBUG", _type, "unknown")
                    continue

            if self.debugMode:
                print("DEBUG", _type, _name)
            if _type == UnityAssetType.Sprite.value:
                self.__extractSprite(obj)
            elif _type == UnityAssetType.Texture2D.value:
                self.__extractTexture2D(obj)
            elif _type == UnityAssetType.TextAsset.value:
                self.__extractTextAsset(obj, _name)
            elif _type == UnityAssetType.MonoBehaviour.value:
                self.__extractMonoBehaviour(obj)
            elif _type == UnityAssetType.Mesh.value:
                self.__extractMesh(obj)

            # log the asset file
            assetFiles.append(_name)

            pass
        return assetFiles

    # =====================================================
    # Helpers
    # =====================================================

    # Creates the directory on your filesystem and it returns the path to reuse on your code
    def __createDestinationPath(self, obj) -> str:
        if self.tempBundlePath is None:
            container = obj.container
            if container is None:
                container = "none"
            dest = os.path.join(self.destinationPath, os.path.dirname(container))
        else:
            dest = os.path.join(self.destinationPath, self.tempBundlePath)
        os.makedirs(os.path.dirname(dest + "/"), exist_ok=True)
        return dest

    # General extract image method
    def __extractImage(self, obj, forceOverwrite: bool = False):
        data = obj.read()
        dest = self.__createDestinationPath(obj) 
        dest += "/" + data.name + ".png"
        if (forceOverwrite or not os.path.exists(dest)):
            try:
                data.image.save(dest)
            except SystemError as se:
                print("ERROR CANNOT EXTRACT IMAGE", se)
        pass

    def __extractSprite(self, obj):
        self.__extractImage(obj)

    def __extractTexture2D(self, obj):
        try:
            self.filterTexture2D(obj)
        except Exception as e:
            self.__extractImage(obj)

    def __extractTextAsset(self, obj, alternativeName = ''):
        name = ""
        if obj.name is None:
            basename = ""
            if obj.container is None:
                basename = alternativeName
            else:
                basename = os.path.basename(obj.container)
            name = "/" + basename
        else:
            name = obj.name
        with open(self.__createDestinationPath(obj) + name, "wb") as f:
            data = obj.read()
            f.write(data.script)

    def __extractMonoBehaviour(self, obj):
        data = obj.read()
        name = data.name
        if name is None or name == "":
            name = "MonoBehaviour"
        outPath = self.__createDestinationPath(obj) + "/" + name + ".json"
        
        if obj.serialized_type.nodes:
            # save decoded data
            tree = obj.read_typetree()
            fp = outPath
            with open(fp, "wt", encoding = "utf8") as f:
                json.dump(tree, f, ensure_ascii = False, indent = 4)
        else:
            # save raw relevant data (without Unity MonoBehaviour header)
            data = obj.read()
            fp = outPath.replace(".json", ".bin")
            with open(fp, "wb") as f:
                f.write(data.raw_data)

        # edit
        if obj.serialized_type.nodes:
            tree = obj.read_typetree()
            # apply modifications to the data within the tree
            obj.save_typetree(tree)
        else:
            with open(self.__createDestinationPath(obj) + "/", data.name) as f:
                data.save(raw_data = f.read())
        return

    def __extractMesh(self, obj):
        mesh = obj.read()
        dest = f"{self.__createDestinationPath(obj)}/{mesh.name}.obj"
        with open(dest, "wt") as f:
            try:
                f.write(mesh.export())
            except Exception as e:
                print("ERROR CANNOT EXPORT MESH DUE TO", e)
        return

    def __filterTexture2D(self, obj):
        raise NotImplementedError("abstract")