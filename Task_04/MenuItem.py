class MenuItem:
    def __init__(self, itemId, name, description, price, category):
        self.__itemId = itemId
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__isAvailable = True

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    @property
    def itemId(self):
        return self.__itemId

    def getItemInfo(self):
        text = f"Item Name: {self.__name} \nItem Description: {self.__description} \nItem Price: {self.__price} \nItem Category: {self.__category} \nItem Availability: {'Available' if self.__isAvailable else 'Nonavailable'}"
        return text