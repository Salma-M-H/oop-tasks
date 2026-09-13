class Customer:
    def __init__(self, customerId, name, phone, email, driversLicenseNumber):
        self.__customerId = customerId
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__driversLicenseNumber = driversLicenseNumber

    @property
    def customerId(self):
        return self.__customerId

    @property
    def name(self):
        return self.__name

    def getCustomerInfo(self):
        text = f"Customer Id: {self.__customerId}\nName: {self.__name}\nPhone: {self.__phone}\nEmail: {self.__email}\nDriver License Number: {self.__driversLicenseNumber}"
        return text