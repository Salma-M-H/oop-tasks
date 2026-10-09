from Enums import ReservationStatus, RoomStatus

class Reservation:
    def __init__(self, reservationId, guest, room, checkInDate, checkOutDate, totalGuests):
        self.__reservationId = reservationId
        self.__guest = guest
        self.__room = room
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__status = ReservationStatus.CONFIRMED
        self.__service = []
        self.__totalGuests = totalGuests
        self.__finalCost = 0

    @property
    def reservationId(self):
        return self.__reservationId

    @property
    def guest(self):
        return self.__guest

    @property
    def checkInDate(self):
        return self.__checkInDate

    @property 
    def checkOutDate(self):
        return self.__checkOutDate

    @property
    def room(self):
        return self.__room

    @property
    def status(self):
        return self.__status

    @property
    def finalCost(self):
        return self.__finalCost

    @finalCost.setter
    def finalCost (self, cost):
        self.__finalCost = cost

    def getNumberOfNights(self):
        return (self.__checkOutDate - self.__checkInDate).days # date handling

    def getRoomCost(self):
        return round(self.__room.getPrice() * self.getNumberOfNights(), 2)
    
    def getServicesCost(self):
        cost = 0
        for service in self.__service:
            servicePrice = service.getPrice()
            cost += servicePrice

        return round(cost, 2)

    def getTotal(self):
        totalAfterDiscount = (self.getRoomCost() + self.getServicesCost()) * (1 - self.guest.getDiscountRate())
        return round(totalAfterDiscount, 2)

    def addService(self, service):
        self.__service.append(service)

    def checkIn(self):
        self.__status = ReservationStatus.CHECKED_IN
        self.__room.changeStatus(RoomStatus.OCCUPIED)

    def checkOut(self):
        self.__status = ReservationStatus.CHECKED_OUT
        self.__room.changeStatus(RoomStatus.AVAILABLE)
        self.__finalCost = self.getTotal()
        return self.__finalCost

    def cancel(self):
        self.__status = ReservationStatus.CANCELLED
        self.__room.changeStatus(RoomStatus.AVAILABLE)

    def getReservationDetails(self):
        header = "=== Reservation Details ===\n"
        reservationId = f"Reservation Id: {self.__reservationId}\n"
        guest = f"Guest: {self.__guest.name} ({self.__guest.guestId})\n"
        emailAndPhone = f"Email: {self.__guest.email}, Phone: {self.__guest.phone}\n"
        room = f"Room: {self.__room.roomNumber} ({self.__room.type.value}) - Floor {self.__room.floor}\n"
        checkIn = f"Check-in: {self.__checkInDate}\n"
        checkout = f"Check-out: {self.__checkOutDate}\n"
        nights = f"Nights: {self.getNumberOfNights()}\n"
        numberOfGuests = f"Number of Guests: {self.__totalGuests}\n"
        status = f"Status: {self.__status.value}\n\n"

        services = "Services: \n"
        servicesList = [f"- {service.name}: ${service.getPrice()}" for service in self.__service]
        serviceStr = '\n'.join(servicesList)

        text = header + reservationId + guest + emailAndPhone + room + checkIn + checkout + nights + numberOfGuests + status + services + serviceStr
        return text


    

    