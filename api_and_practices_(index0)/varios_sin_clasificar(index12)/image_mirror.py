from PIL import Image
Image.open('binodd.jpg') #original Image 

img = Image.open('binodd.jpg')
Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r'binodd_mirror.png')
Image.open('binodd_mirror.png') #Mirrored Image


