import os
import argparse
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('directory')
arguments = parser.parse_args()

directory = os.fsencode(arguments.directory)
count = 0

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith('.webp'):
        image = Image.open(f'{arguments.directory + "/" + filename}')
        new_filename = filename.split()[0] + '.png'
        image.save(f'{new_filename}', format='PNG')
