import datetime
from Rental import Rental

class RentalAgency:
    def __init__(self, agencyName):
        self.__agencyName = agencyName
        self.__vehicles = []
        self.__customers = []
        self.__rentals = []

    def addVehicle(self, vehicle): 
        self.__vehicles.append(vehicle)

    def registerCustomer(self, customer):
        self.__customers.append(customer)

    def getAvailableVehicles(self):
        availableCars = [vehicle for vehicle in self.__vehicles if vehicle.isAvailable]
        return availableCars

    def __checkCustomerRegister(self, customer):
        for cust in self.__customers:
            if customer.customerId.lower() == cust.customerId.lower():
                return 
        else:
            self.registerCustomer(customer)

    def createRental(self, customer, vehicle, days): 

        self.__checkCustomerRegister(customer)

        if vehicle.isAvailable:
            vehicle.rent()
        else:
            print("The car is not available")
            return 

        start_date = datetime.date.today()
        days = datetime.timedelta(days=days)
        end_date = start_date + days

        rental_id = f"R{len(self.__rentals)+1:03d}"
        rental = Rental(rental_id, customer, vehicle, start_date, end_date)

        self.__rentals.append(rental)

        return rental
                

    def completeRental(self, rentalId):
        for rental in self.__rentals:
            if rental.rentalId.lower() == rentalId.lower():
                rental.completeRental()
                return rental.getTotalCost()
                

    def getActiveRentals(self):
        activeRentals = [rental for rental in self.__rentals if rental.isActive]
        return activeRentals

    def getCustomerRentals(self, customerId):
        rentals = []
        for rental in self.__rentals:
            if customerId.lower() == rental.customer.customerId.lower():
                rentals.append(rental)

        return rentals

    def displayFleet(self):
        print(f'=== {self.__agencyName} - Fleet Status ===')
        for vehicle in self.__vehicles:
            print(vehicle.getVehicleInfo())