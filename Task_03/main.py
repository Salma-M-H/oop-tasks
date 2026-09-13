from Customer import Customer
from Rental import Rental
from Rental_Agency import RentalAgency
from Vehicle import Vehicle

# Create rental agency
agency =   RentalAgency("Prime Car Rentals")

# Add vehicles to fleet
car1 =   Vehicle("V001", "Toyota", "Camry", 2022, 45.00)
car2 =   Vehicle("V002", "Honda", "Accord", 2023, 50.00)
car3 =   Vehicle("V003", "Tesla", "Model 3", 2023, 85.00)


agency.addVehicle(car1)
agency.addVehicle(car2)
agency.addVehicle(car3)


# # Register customers
customer1 =   Customer("C001", "Alice Johnson", "555-0123",
                        "alice@email.com", "DL123456")
customer2 =   Customer("C002", "Bob Smith", "555-0456",
                        "bob@email.com", "DL789012")


agency.registerCustomer(customer1)
agency.registerCustomer(customer2)


# agency.displayFleet()
# print()

rental1 = agency.createRental(customer1, car1, 5)
# print("Rental created: " + rental1.rentalId)
# print("Total Cost: $", rental1.getTotalCost())

rental2 = agency.createRental(customer2, car3, 3)
# print("Rental created: " + rental2.rentalId)
# print("Total Cost: $", rental2.getTotalCost())

# # Display available vehicles after rentals
# print("After rentals:")
# agency.displayFleet()

# # Complete a rental
# agency.completeRental(rental1.rentalId)
# print("Rental " + rental1.rentalId + " completed!")

# # Display customer rental history
# customerRentals = agency.getCustomerRentals("C001")
# print("Alice's rental history:", len(customerRentals), "rental(s)")
