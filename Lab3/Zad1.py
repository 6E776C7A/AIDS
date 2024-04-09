import os, shutil

directory = '/home/student/Desktop/lab3/zadanie1'
directory_folders = '/home/student/Desktop/lab3'
#wczytanie plików
files = os.listdir(directory)

for items in files:
    path = os.path.join(directory_folders, items[0])
    #tworzenie folderów
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    #zmiana ścieżki dla plików do stworzonych folderów
    path_dest = os.path.join(path, items)
    path_source = os.path.join(directory, items)
    if items[0] == path[len(path)-1]:
        shutil.move(path_source, path_dest)