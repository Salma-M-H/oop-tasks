from enum import Enum

class RoomType(Enum):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    SUITE = 'Suite'
    DELUXE = 'Deluxe'
    PRESIDENTIAL = 'Presidential'

class RoomStatus(Enum):
    AVAILABLE = 'Available'
    OCCUPIED = 'Occupied'
    UNDER_MAINTENANCE = 'UnderMaintenance'
    RESERVED = 'Reserved'

class ReservationStatus(Enum):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CHECKED_IN = 'CheckIn'
    CHECKED_OUT = 'CheckOut'
    CANCELLED = 'Cancelled'


