import os
import argparse
from src.Converter import Converter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory')
    arguments = parser.parse_args()
    conv = Converter()

    directory = os.fsencode(arguments.directory)
    count = 0

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        if filename.endswith('.webp'):
            conv.convert(f"{arguments.directory + '/' + filename}")

if __name__== '__main__':
    main()
