from Ichargeable import IChargeable
from Enums import RoomStatus, RoomType

class Room(IChargeable):

    def __init__(self, roomNumber, type, floor, pricePerNight, maxOccupancy):
        self.__roomNumber = roomNumber
        self.__type = type
        self.__status = RoomStatus.AVAILABLE
        self.__floor = floor
        self.__pricePerNight = pricePerNight
        self.__maxOccupancy = maxOccupancy
        self.__amenities = []

    @property
    def type(self):
        return self.__type

    @property
    def status(self):
        return self.__status

    @property
    def roomNumber(self):
        return self.__roomNumber

    @property
    def pricePerNight(self):
        return self.__pricePerNight

    @property
    def floor(self):
        return self.__floor

    @property
    def maxOccupancy(self):
        return self.__maxOccupancy

    def getPrice(self):
        return self.__pricePerNight

    def getDescription(self):
        roomNumber = f"Room Number: {self.__roomNumber} - Floor ({self.__floor})\n"
        roomType = f"Room Type: {self.__type.value}\n"
        roomStatus = f"Room Status: {self.__status.value}\n"
        price = f"Price Per Night: ${self.__pricePerNight}\n"
        maxOccupancy = f"Max Occupancy: {self.__maxOccupancy}\n"

        text = roomNumber + roomType + roomStatus + price + maxOccupancy
        return text


    def isAvailable(self):
        if self.__status == RoomStatus.AVAILABLE:
            return True
        return False

    def changeStatus(self, newStatus):
        if newStatus in RoomStatus:
            self.__status = newStatus
        else:
            print('Wrong Status')