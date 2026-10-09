from Ichargeable import IChargeable

class Service(IChargeable):
    def __init__(self, serviceId, name, price, description):
        self.__serviceId = serviceId
        self.__name = name
        self.__price = price
        self.__description = description

    @property
    def name(self):
        return self.__name
    

    def getPrice(self):
        return self.__price

    def getDescription(self):
        serviceId = f"Service Id: {self.__serviceId}\n"
        name = f"Service Name: {self.__name}\n"
        price = f"Service Price: {self.__price}\n"
        description = f"Service Description: {self.__description}\n"

        text = serviceId + name + price + description
        return text