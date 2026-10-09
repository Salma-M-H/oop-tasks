class Guest:
    def __init__(self, guestId, name, email, phone, idNumber, loyaltyPoints):
        self.__guestId = guestId
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__idNumber = idNumber
        self.__loyaltyPoints = loyaltyPoints

    @property
    def guestId(self):
        return self.__guestId

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    def getGuestInfo(self):
        name = f"Guest: {self.__name} ({self.__guestId})\n"
        emailAndPhone = f"Email: {self.__email}, Phone: {self.__phone}\n"
        idNumber = f"Id Number: {self.__idNumber}\n"
        points = f"Loyalty Points: {self.__loyaltyPoints}\n"

        text = name + emailAndPhone + idNumber + points
        return text

    def addLoyaltyPoints(self, points):
        self.__loyaltyPoints += points

    def getDiscountRate(self):
        return (self.__loyaltyPoints * 2) / 10000

    def zeroLoyaltyPoints(self):
        self.__loyaltyPoints = 0