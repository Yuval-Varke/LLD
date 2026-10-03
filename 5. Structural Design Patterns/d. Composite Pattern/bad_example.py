from typing import List


class File:
    def __init__(self, name: str):
        self.__name = name

    def show_details(self):
        return f"File : {self.__name}"


class Folder:
    def __init__(self, name: str):
        self.__name = name
        self.__files: List[File] = []

    def add_file(self, file: File):
        self.__files.append(file)

    def show_details(self):
        print(f"Folder name: {self.__name}")
        for file in self.__files:
            print(file.show_details())


file1 = File("image.png")
file2 = File("ppt")
file3 = File("word.exe")

folder = Folder("my_drive")

folder.add_file(file1)
folder.add_file(file2)
folder.add_file(file3)

folder.show_details()