class OrderItem:
    def __init__(self, itemId, menuItem, quantity, specialInstructions=''):
        self.__itemId = itemId
        self.__menuItem = menuItem
        self.__quantity = quantity
        self.__specialInstructions = specialInstructions

    @property
    def itemId (self):
        return self.__itemId

    @property
    def menuItem(self):
        return self.__menuItem

    @property
    def quantity(self):
        return self.__quantity

    def getSubTotal(self): 
        return self.__quantity * self.__menuItem.price
    
    def getOrderItemDetails(self): 
        # text = f"Order Item Name: {self.__menuItem.name} \nOrder Item Description: {self.__menuItem.description} \nOrder Item Category: {self.__menuItem.category} \nOrder Item Quantity: {self.__quantity} \nOrder Item Price: {self.getSubTotal()} \nInstructions: {self.__specialInstructions if self.__specialInstructions else 'No Instructions'}"
        text = f"- {self.__menuItem.name} x{self.__quantity}- {self.getSubTotal()} \n Special: {self.__specialInstructions if self.__specialInstructions else 'No instructions'}"
        return text