import datetime
from Order import Order
from Menu import Menu

class Restaurant:

    def __init__(self, restaurantName, taxRate):
        self.__restaurantName = restaurantName
        self.__menu = Menu(restaurantName)
        self.__orders = []
        self.__taxRate = taxRate


    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, item):
        self.__menu.addMenuItem(item)

    @property
    def taxRate(self):
        return self.__taxRate

    def createOrder(self, tableNumber):
        orderId = f"ORD{len(self.__orders)+1:03d}"
        orderItems = [] 
        orderTime = datetime.datetime.now()
        status = 'Pending'

        order = Order(orderId, tableNumber, orderItems, orderTime, status)
        self.__orders.append(order)

        return order

    def getOrder(self, orderId):
        for order in self.__orders:
            if order.orderId.lower() == orderId.lower():
                return order

    def getOrdersByStatus(self, status):
        orders = []
        for order in self.__orders:
            if order.status.lower() == status.lower():
                orders.append(order)
        return orders

    def getActiveOrders(self):
        activeOrders = [order for order in self.__orders if order.status.lower() != 'completed']
        return activeOrders
    
    def completeOrder(self, orderId):
        for order in self.__orders:
            if orderId.lower() == order.orderId.lower():
                order.updateStatus('Completed')
                break

    def getTotalRevenue(self):
        cost = 0.0
        for order in self.__orders:
            if order.status.lower() == 'completed':
                cost += order.getTotal(self.__taxRate)
        return cost
    
    def getPopularItems(self, count):
        countDict = {}
        for order in self.__orders:
            for orderItem in order.orderItems:
                menuItemName = orderItem.menuItem.name
                if menuItemName in countDict.keys():
                    countDict[menuItemName] += orderItem.quantity

                else:
                    countDict[menuItemName] = orderItem.quantity
                    
        # problem => it will give me all the popular items that may not match the count value
        maxValues = sorted(countDict.values(), reverse=True)
        maxCounts = maxValues[0:count]
        # max ordered but not sorted by count 
        name = [key for key, value in countDict.items() if value in maxCounts]

        return name


