# Code snippet taken from @clcoding on Twitter / clcoding.com
# Credits: https://github.com/danielgatis/rembg

from rembg import remove
from PIL import Image
input_path = 'coffee-mug.jpg'
output_path = 'coffee-mug.png'
img = Image.open(input_path)
output = remove(img)
output.save(output_path)