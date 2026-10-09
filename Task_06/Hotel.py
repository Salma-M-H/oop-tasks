from Reservation import Reservation
from Enums import RoomStatus, ReservationStatus

class Hotel:
    def __init__(self, hotalName, address):
        self.__hotelName = hotalName
        self.__address =address
        self.__rooms = []
        self.__reservations = []
        self.__guests = []
        self.__availableServices = []

    @property
    def availableServices(self):
        return self.__availableServices

    def addRoom(self, room):
        self.__rooms.append(room)

    def registerGuest(self, guest):
        self.__guests.append(guest)

    def addService(self, service):
        self.__availableServices.append(service)

    def getAvailableRooms(self, checkIn, checkOut):
        rooms = []
        for reservation in self.__reservations:
            if reservation.status != ReservationStatus.CANCELLED:
                if not ((checkIn >= reservation.checkOutDate) or (checkOut <= reservation.checkInDate)):
                    rooms.append(reservation.room)

        availableRooms = []
        for room in self.__rooms:

            if (room not in rooms) and (room.status == RoomStatus.AVAILABLE):
                availableRooms.append(room)

        return availableRooms


    def getAvailableRoomsByType(self, type, checkIn, checkOut):
        availableRooms = self.getAvailableRooms(checkIn, checkOut)
        availableRoomsByType = []

        for room in availableRooms:
            if room.type == type:
                availableRoomsByType.append(room)

        return availableRoomsByType


    def createReservation(self, guest, room, checkIn, checkOut, guests):
        reservationId = f"R{len(self.__reservations)+1:03d}"

        if guest not in self.__guests:
            self.registerGuest(guest)

        availableRooms = self.getAvailableRooms(checkIn, checkOut)
        if room not in availableRooms:
            return 'The rooms is not available'

        if checkIn > checkOut:
            return "Time Error (Check in date after the check out)"
        elif checkIn == checkOut:
            return "Time Error (check in the same as check out)"

        if guests > room.maxOccupancy:
            return "Exceed Room's Maximum Occupancy"

        reservation = Reservation(reservationId, guest, room, checkIn, checkOut, guests)
        self.__reservations.append(reservation)
        return reservation


    def __findReservationHelper(self, reservationId):
        for reservation in self.__reservations:
             if reservation.reservationId.lower() == reservationId.lower():
                 return reservation

    def cancelReservation(self, reservationId):
        reservation = self.__findReservationHelper(reservationId)
        reservation.cancel()

    def checkInGuest(self, reservationId):
        reservation = self.__findReservationHelper(reservationId)
        reservation.checkIn()
        
    def checkOutGuest(self, reservationId):
        reservation = self.__findReservationHelper(reservationId)
        payment = reservation.checkOut()
        reservation.guest.zeroLoyaltyPoints()
        loyaltyPoints = int(payment/10)
        reservation.guest.addLoyaltyPoints(loyaltyPoints)
        return payment, loyaltyPoints

    def getReservationsByGuest(self, guestId):
        reservations = []
        for reservation in self.__reservations:
            if reservation.guest.guestId.lower() == guestId.lower():
                reservations.append(reservation)

        return reservations


    def getCurrentOccupancy(self):
        numberOfOccupiedRooms = 0
        for room in self.__rooms:
            if room.status == RoomStatus.OCCUPIED:
                numberOfOccupiedRooms += 1
        OccupiedRoomsPercentage = (numberOfOccupiedRooms / len(self.__rooms)) * 100
        return OccupiedRoomsPercentage


        
    def getRevenue(self, startDate, endDate):
        cost = 0 

        for reservation in self.__reservations:
            if reservation.status == ReservationStatus.CHECKED_OUT:

                if startDate <= reservation.checkOutDate <= endDate:
                    cost += reservation.finalCost

        return cost
                    

    def displayHotelStatus(self):
        numberOfRooms = len(self.__rooms)
        percentOfOccupiedRooms = self.getCurrentOccupancy()
        numberOfOccupiedRooms = int(numberOfRooms * (percentOfOccupiedRooms/100))

        numberOfAvailableRooms = len([room for room in self.__rooms if room.isAvailable()])
        percentOfAvailableRooms = (numberOfAvailableRooms / numberOfRooms) * 100

        listOfActiveReservations = [reservation for reservation in self.__reservations if reservation.status == ReservationStatus.CHECKED_IN]
        listOfMaintenanceRooms = [room for room in self.__rooms if room.status == RoomStatus.UNDER_MAINTENANCE]


        header = f"=== {self.__hotelName.title()} Status ===\n"
        rooms = f"Total Rooms: {numberOfRooms}\n"
        AvailableRooms = f"Available Rooms: {numberOfAvailableRooms} ({percentOfAvailableRooms}%)\n"
        OccupiedRooms = f"Occupied: {numberOfOccupiedRooms} ({percentOfOccupiedRooms}%)\n"
        underMaintanence = f"Under Maintanence: {len(listOfMaintenanceRooms)}\n"
        CurrentOccupancy = f"Current Occupancy: {percentOfOccupiedRooms}\n"
        activeReservations = f"Active Reservations: {len(listOfActiveReservations)}"

        text = header + rooms + AvailableRooms + OccupiedRooms + underMaintanence + CurrentOccupancy + activeReservations
        print(text)

    
    