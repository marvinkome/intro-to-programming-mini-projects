import os
import re

def rename_file():
    all_files = os.listdir('C:\\Users\\yyy\\Music\\')
    #print(all_files)
    saved_path = os.getcwd()
    os.chdir('C:\\Users\\yyy\\Music\\')

    for file in all_files:
        file_name = file.split('.')[0]
        file_name = re.sub('[0-9]', '', file_name)
        file_name = file_name + '.mp3'

        print(file_name)
        os.rename(file, file_name + '.mp3')

    os.chdir(saved_path)

rename_file()
