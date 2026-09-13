class Rental:
    def __init__(self, rentalId, customer, vehicle, startDate, endDate):
        self.__rentalId = rentalId
        self.__customer = customer
        self.__vehicle = vehicle
        self.__startDate = startDate
        self.__endDate = endDate
        self.__isActive = True

    @property
    def rentalId(self):
        return self.__rentalId

    @property
    def isActive(self):
        return self.__isActive

    @property
    def customer(self):
        return self.__customer

    def getRentalDuration(self):
        return (self.__endDate - self.__startDate).days
    
    def getTotalCost(self):
        return self.getRentalDuration() * self.__vehicle.dailyRate

    def completeRental(self):
        self.__isActive = False
        self.__vehicle.returnVehicle()

    def getRentalInfo(self):
        text = f"Rental Id: {self.__rentalId}\nCustomer Name: {self.__customer.name}\nVehicle Model: {self.__vehicle.model}\nStart Date: {self.__startDate}\nEnd Date: {self.__endDate}\nActive: {self.__isActive}"
        return text
