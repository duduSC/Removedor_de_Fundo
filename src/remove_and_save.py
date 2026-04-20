
from PIL import Image
from rembg import remove

class RemoveAndSave():

    def __init__(self):
        pass 

    def read(self,path):
         return Image.open(path)

    def troca_formato(self,im):
        """Troca o formato para png"""
        file, formato = im.filename.split(".")
        return file + ".png"  

    def process(self,imagem) -> Image:
        try:
                new_image = remove(imagem)
                return new_image
        except Exception as error:
            print(error)