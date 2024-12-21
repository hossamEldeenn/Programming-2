from abc import ABC,abstractmethod

class Machine(ABC):
    @abstractmethod
    def Print(self):
        pass
    
    @abstractmethod
    def Scan(self):
        pass
    
    @abstractmethod
    def Fax(self):
        pass


class MultiFunctionPrinter(Machine):
    def Print(self):
        return 'Printing Doucument'
    
    def Scan(self):
        return 'Scanning Document'
    
    def Fax(self):
        return 'Faxing Document'
    

class SimplePrinter(Machine):
    def Print(self):
        return 'Printing Doucument'
    
    def Scan(self):
        raise NotImplementedError("This printer can't scan")
        
    def Fax(self):
        raise NotImplementedError("This printer can't fax")
        