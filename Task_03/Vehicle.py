class Vehicle:
    def __init__(self, vehicleId, make, model, year, dailyRate):
        self.__vechicleId = vehicleId
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__isAvailable = True

    @property
    def isAvailable(self):
        return self.__isAvailable

    @property
    def dailyRate(self):
        return self.__dailyRate

    @property
    def model(self):
        return self.__model

    def getVehicleInfo(self): 
        text = f"{self.__vechicleId} - {self.__year} {self.__make} {self.__model} - ${self.__dailyRate:.2f}/day - {'Available' if self.__isAvailable else 'Not Available'}"
        return text

    def rent(self):
        if self.__isAvailable:
            self.__isAvailable = False
        else:
            return
        
    def returnVehicle(self): 
        self.__isAvailable = True
        
    def calculateRentalCost(self, days):
        return days * self.__dailyRate