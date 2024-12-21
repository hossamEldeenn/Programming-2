from abc import ABC,abstractmethod

class Printable(ABC):
    @abstractmethod
    def Print(self):
        pass


class Scanable(ABC):
    @abstractmethod
    def Scan(self):
        pass
    

class Faxable(ABC):
    @abstractmethod
    def Fax(self):
        pass
    

class MultiFunctionPrinter(Printable,Scanable,Faxable):
    def Print(self):
        return 'Printing Doucument'
    
    def Scan(self):
        return 'Scanning Document'
    
    def Fax(self):
        return 'Faxing Document'
 
    
class SimplePrinter(Printable):
    def Print(self):
        return 'Printing Doucument'

