import shutil # Mover
from os import listdir # Mover
from os.path import isfile, join, basename # Mover
def move(path_origem, path_destino, ext='csv'): # Extensão que deseja mover
                for item in [join(path_origem, f) for f in listdir(path_origem) if isfile(join(path_origem, f)) and f.endswith(ext)]:
                    # print(item)
                    shutil.move(item, join(path_destino, basename(item)))
                    print('moved "{}" -> "{}"'.format(item,
                        join(path_destino, basename(item))))
if __name__ == '__main__':
                move('(Local onde o arquivo esta)','(Local para onde sera movido)')
