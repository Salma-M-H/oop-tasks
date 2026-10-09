from Hotel import Hotel
from Room import Room
from Enums import *
from Service import Service
from Guest import Guest
import datetime


def findServiceByName(services, service_name):
    for service in services:
        if service.name.lower() == service_name.lower():
            return service 


# Create hotel
hotel = Hotel("Grand Plaza Hotel", "123 Main Street, City")

# Create rooms
room1 = Room("101", RoomType.SINGLE, 1, 89.99, 1)
room2 = Room("201", RoomType.DOUBLE, 2, 129.99, 2)
room3 = Room("301", RoomType.SUITE, 3, 249.99, 4)
room4 = Room("401", RoomType.DELUXE, 4, 349.99, 3)

# print(room4.getPrice())
# print(room4.isAvailable())
# room4.changeStatus(RoomStatus.OCCUPIED) 
# print(room4.isAvailable())
# print(room4.getDescription())

hotel.addRoom(room1)
hotel.addRoom(room2)
hotel.addRoom(room3)
hotel.addRoom(room4)
# #######################################################################

# # Create Services
service1 = Service("S001", "Room Service", 25.00, "24-hour room service")
service2 = Service("S002", "Spa Treatment", 100.00, "90-minute massage")
service3 = Service("S003", "Airport Shuttle", 50.00, "Round trip airport transfer")
service4 = Service("S004", "Breakfast Buffet", 20.00, "Continental breakfast")

# print(service1.getPrice())
# print(service1.getDescription())

hotel.addService(service1)
hotel.addService(service2)
hotel.addService(service3)
hotel.addService(service4)

# # Create Guests
guest1 = Guest("G001", "Alice Johnson", "alice@email.com", "555-0123", "ID123456", 250)
guest2 = Guest("G002", "Bob Smith", "bob@email.com", "555-0456", "ID789012", 100)

# print(guest1.getGuestInfo())


hotel.registerGuest(guest1)
hotel.registerGuest(guest2)

# # Check Available rooms
checkIn = datetime.date.today() + datetime.timedelta(7)
checkOut = checkIn + datetime.timedelta(3)

availableRooms = hotel.getAvailableRooms(checkIn, checkOut)
print(f"Available rooms for {checkIn} to {checkOut}: ")
for room in availableRooms:
    print(f"- Room {room.roomNumber} {room.type} ${room.pricePerNight}/night")

availableRoomsByType = hotel.getAvailableRoomsByType(RoomType.SUITE, checkIn, checkOut)
print(f"Available rooms for {checkIn} to {checkOut}: ")
for room in availableRoomsByType:
    print(f"- Room {room.roomNumber} {room.type} ${room.pricePerNight}/night")

reservation = hotel.createReservation(guest1, availableRoomsByType[0], checkIn, checkOut, 2)
print("\nReservation created: " ,reservation.reservationId)

# print(reservation.getNumberOfNights())
# print(reservation.getRoomCost())
# print(reservation.getServicesCost())
# print(reservation.getTotal())


reservation.addService(findServiceByName(hotel.availableServices, "Breakfast Buffet"))
reservation.addService(findServiceByName(hotel.availableServices, "Airport Shuttle"))

# print(reservation.getServicesCost())
# print(reservation.getTotal())


print(reservation.getReservationDetails())


# # Calculate total
print("\nReservation Summary:")
print(f"Room Cost ({reservation.getNumberOfNights()} nights): ${reservation.getRoomCost()}")
print(f"Services Cost: ${reservation.getServicesCost():0.2f}")
print(f"Guest Discount: {(guest1.getDiscountRate())*100}%")
print(f"Total: ${reservation.getTotal()}")

# print("\nGuest checked in. Room " + availableRoomsByType[0].roomNumber + " status: " + availableRoomsByType[0].status.value)


# hotel.displayHotelStatus()

payment, loyaltyPoints = hotel.checkOutGuest(reservation.reservationId)
print(f"\nGuest checked out. Final bill: ${payment:.02f}")
print(f"Loyalty points earned: {loyaltyPoints}")
