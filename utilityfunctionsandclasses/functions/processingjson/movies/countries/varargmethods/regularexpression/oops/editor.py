from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def edit(self):
        pass
    @abstractmethod
    def save(self):
        pass

class VsCode(Editor):

    def debug(self):
        print("vscode debug")

    def edit(self):
        print("vscode edit")

    def save(self):
        print("vscode save" )

obj=VsCode()
obj.debug()
obj.edit()
obj.save()
