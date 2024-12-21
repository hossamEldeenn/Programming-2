from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> None:
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self) -> None:
        pass


class Document(Printable):
    def __init__(self, content: str):
        self.content = content

    def Print(self) -> None:
        print(self.content)
        
        
class Image(Scannable, Faxable):
    def __init__(self, data: bytes):
        self.data = data

    def scan(self) -> None:
        print("Scanning the image")

    def fax(self) -> None:
        print("Faxing the image")


class Printer:
    def print(self, printable: Printable) -> None:
        printable.print()


class ScannerFaxer:
    def scan_and_fax(self, scannable: Scannable, faxable: Faxable) -> None:
        scannable.scan()
        faxable.fax()