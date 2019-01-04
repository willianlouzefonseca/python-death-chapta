from configparser import SafeConfigParser
config = SafeConfigParser()

config.read('config.ini')

config.

config.add_section('images')
config.set('images', 'imagens_directory', '/home/willian/Desktop/tesserpython/images-tesser/')
config.set('images', 'image_name_to_convert', 'imagem.asp.gif')
config.set('images', 'image_name_converted', 'image.png')


with open('config.ini', 'w') as f:
    config.write(f)