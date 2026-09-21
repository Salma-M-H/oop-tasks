from OrderItem import OrderItem
import datetime

class Order:
    def __init__(self, orderId, tableNumber, orderItems, orderTime, status):
        self.__orderId = orderId
        self.__tableNumber = tableNumber
        self.__orderItems = orderItems
        self.__orderTime = orderTime
        self.__status = status

    @property
    def orderId(self):
        return self.__orderId

    @property
    def status(self):
        return self.__status

    @property
    def orderItems(self):
        return self.__orderItems

    def addItem(self, menuItem, quantity, instructions=''):
        orderItemId = f"OI{len(self.__orderItems)+1:03d}"
        orderItem = OrderItem(orderItemId, menuItem, quantity, instructions)
        self.__orderItems.append(orderItem)
        
    def removeItem(self, itemId):
        self.__orderItems = [item for item in self.__orderItems if item.itemId.lower() != itemId.lower()]
        

    def getSubTotal(self):
        cost = 0
        for orderItem in self.__orderItems:
            cost += orderItem.getSubTotal()
        return round(cost, 2)

    def getTax(self, tax):
        return round(self.getSubTotal() * tax, 2)

    def getTotal(self, tax): 
        return round(self.getSubTotal() + self.getTax(tax), 2)

    def calculateTip(self, percentage):
        return round(self.getSubTotal() * (percentage), 2)

    def updateStatus(self, newStatus):
        self.__status = newStatus

    def getOrderSummary(self):
        text = "\n\n".join([orderItem.getOrderItemDetails() for orderItem in self.__orderItems])
        main_text = f"Order Id: {self.__orderId} \nTable: {self.__tableNumber} \nTime: {self.__orderTime} \nStatus: {self.__status} \n\nItems:\n{text}"
        return main_text
        
        