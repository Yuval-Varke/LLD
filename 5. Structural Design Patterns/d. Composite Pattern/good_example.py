from typing import List
from abc import ABC, abstractmethod

class FileSystemComponent:
    @abstractmethod
    def show_details(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name

    def show_details(self):
        return f"File : {self.__name}"


class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.__name = name
        self.__components: List[FileSystemComponent] = []

    def add_component(self, component: FileSystemComponent):
        self.__components.append(component)

    def show_details(self):
        print(f"Folder name: {self.__name}")
        for component in self.__components:
            print(component.show_details())


file1 = File("image.png")
file2 = File("ppt")
file3 = File("word.exe")

sub_folder = Folder("sub folder")
sub_folder.add_component(file1)
sub_folder.add_component(file2)
sub_folder.add_component(file3)

image_file = File("imaaageeee")
movie = File("krissh")
main_folder = Folder("main folder")
main_folder.add_component(image_file)
main_folder.add_component(movie)
main_folder.add_component(sub_folder)

main_folder.show_details()