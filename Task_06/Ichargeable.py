from abc import ABC, abstractmethod

class IChargeable(ABC):
    
    @abstractmethod
    def getPrice(self): pass

    @abstractmethod
    def getDescription(self): pass