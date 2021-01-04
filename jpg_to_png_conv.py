from PIL import Image
from sys import argv
import os

dir1 = argv[1]
path = argv[2]

# dir1 = "pokemon_images/"
# path = 'processed_images/'

try:
    os.mkdir(path)
except FileExistsError:
    pass

for subdir, dir2, files in os.walk(dir1):
    for file in files:
        x = os.path.join(subdir, file)
        print(f'converting  {file}', end=' ')
        print(f'to {file.strip(".jpg")}.png')
        img = Image.open(x)
        img.save(f'{path}{file.strip(".jpg")}.png', 'png')
