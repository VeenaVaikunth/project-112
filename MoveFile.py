import os
import shutil

from_dir = './Downloads'
to_dir = './Document_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(path)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension == [".txt", ".doc", "docx", "pdf"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + file_name

    if os.path.exists(path2):
        print('moving...' + file_name)
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print('moving...' + file_name)
        shutil.move(path1, path3)