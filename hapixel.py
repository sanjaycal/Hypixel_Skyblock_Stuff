import hypixel_api

a = hypixel_api.hypixel()

class minion():
    def __init__(self, times_per_action, item1, item2 ="a"):
        self.hypixelObject = a
        self.item1 = item1
        if item1 != 'a':
            self.item2 = item2
        else:
            self.item2 = 'null'
        self.times_per_action = times_per_action
    def Get_Hourly_Money(self, level):
        self.hourlyMoney = (3600/self.times_per_action[level-1])*(self.hypixelObject.get_sell_price(self.item1)+self.hypixelObject.get_sell_price(self.item2))
        return self.hourlyMoney
    
