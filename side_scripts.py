import os
import glob
from config import OUTPUT_PATH


def delete_empty_dirs():
    path = os.path.join(OUTPUT_PATH, 'product_dkp')

    for dir in os.listdir(path):
        dir_path = os.path.join(path, dir)
        if not any(os.scandir(dir_path)):
            print(dir_path)
            os.rmdir(dir_path)


def delete_empty_dirs_with_zero_volume_files():
    path = os.path.join(OUTPUT_PATH, 'product_dkp')

    for file in glob.glob(path + '/*/urls.txt'):
        if os.stat(file).st_size == 0:
            print(file)
            dir_path = os.path.dirname(file)
            os.remove(file)
            os.rmdir(dir_path)


if __name__ == '__main__':
    delete_empty_dirs()
    delete_empty_dirs_with_zero_volume_files()
