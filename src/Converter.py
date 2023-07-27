'''Модуль, содержащий класс по работе с конвертацией изображений.'''

from PIL import Image

class Converter:
    '''Класс, который отвечает за конвертацию изображений формата .webp в иные форматы.
    '''

    def convert(self, filename: str) -> None:
        '''Конвертирует файл с указанным в качестве параметра названием в формат PNG'''
        image = Image.open(filename)
        new_filename = filename.split()[0] + '.png'
        image.save(f'{new_filename}', format='PNG')
