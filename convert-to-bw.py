from PIL import Image
from pathlib import Path

file = Path(__file__).with_name('deer-photo.jpg') 
img = Image.open(file)

img = img.convert("1") #  can be 1, L or LA for B&W, grayscale
img.show()