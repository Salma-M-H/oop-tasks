import re

class Menu:
    def __init__(self, restuarantName):
        self.__restaurantName = restuarantName
        self.__menuItems = []

    def addMenuItem(self, item):
        self.__menuItems.append(item)

    def removeMenuItem(self, itemId):
        self.__menuItems = [Item for Item in self.__menuItems if itemId.lower()!=Item.itemId.lower()]


    def getItemsByCategory(self, category):
        items = [Item.name for Item in self.__menuItems if Item.category.lower() == category.lower()]
        return " - ".join(items)
    
    def searchItem(self, keyword):
        pat = keyword.lower()
        items = []

        for item in self.__menuItems:
            name = item.name.lower()
            res = re.search(pat, name)
            if res:
                items.append(item.name)
        return items

    def displayMenu(self):
        itemsDict = {} 

        for item in self.__menuItems:
            if item.category in itemsDict.keys():
                itemsDict[item.category].append(item.name)

            else:
                itemsDict[item.category] = []
                itemsDict[item.category].append(item.name)


        for category, items in itemsDict.items():
            print(category.title())

            for name in items:
                print(f'\t- {name.title()}')
        
                


        




