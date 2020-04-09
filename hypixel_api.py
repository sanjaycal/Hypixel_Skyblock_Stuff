import requests
import json
import time

# its helpful https://hypixel.net/threads/skyblock-bazzar-api.2675559/

class hypixel():
    def __init__(self):
        self.itemw = [
    "ENCHANTED_RAW_CHICKEN",
    "INK_SACK:3",
    "BROWN_MUSHROOM",
    "ENCHANTED_WATER_LILY",
    "INK_SACK:4",
    "TARANTULA_WEB",
    "CARROT_ITEM",
    "ENCHANTED_POTATO",
    "LOG:1",
    "ENCHANTED_SLIME_BALL",
    "ENCHANTED_GOLDEN_CARROT",
    "LOG:3",
    "LOG:2",
    "ENCHANTED_RABBIT_HIDE",
    "ENCHANTED_GLOWSTONE_DUST",
    "ENCHANTED_INK_SACK",
    "ENCHANTED_CACTUS",
    "ENCHANTED_SUGAR_CANE",
    "ENCHANTED_BIRCH_LOG",
    "ENCHANTED_GUNPOWDER",
    "ENCHANTED_MELON",
    "ENCHANTED_COOKED_SALMON",
    "ENCHANTED_SUGAR",
    "LOG",
    "CACTUS",
    "ENCHANTED_BLAZE_ROD",
    "GHAST_TEAR",
    "ENCHANTED_CAKE",
    "PUMPKIN",
    "ENCHANTED_ENDER_PEARL",
    "PURPLE_CANDY",
    "WHEAT",
    "ENCHANTED_FERMENTED_SPIDER_EYE",
    "ENCHANTED_GOLD_BLOCK",
    "ENCHANTED_RAW_SALMON",
    "ENCHANTED_JUNGLE_LOG",
    "ENCHANTED_FLINT",
    "ENCHANTED_GLISTERING_MELON",
    "IRON_INGOT",
    "PRISMARINE_SHARD",
    "ENCHANTED_EMERALD",
    "ENCHANTED_SPIDER_EYE",
    "ENCHANTED_EMERALD_BLOCK",
    "RED_MUSHROOM",
    "MUTTON",
    "ENCHANTED_MELON_BLOCK",
    "ENCHANTED_CLAY_BALL",
    "DIAMOND",
    "COBBLESTONE",
    "SPIDER_EYE",
    "RAW_FISH",
    "ENCHANTED_PUFFERFISH",
    "GLOWSTONE_DUST",
    "GOLD_INGOT",
    "REVENANT_VISCERA",
    "TARANTULA_SILK",
    "POTATO_ITEM",
    "ENCHANTED_MUTTON",
    "ENCHANTED_HUGE_MUSHROOM_1",
    "SUPER_COMPACTOR_3000",
    "ENCHANTED_IRON",
    "STOCK_OF_STONKS",
    "ENCHANTED_COBBLESTONE",
    "ENCHANTED_BONE",
    "ENCHANTED_PAPER",
    "ENCHANTED_HUGE_MUSHROOM_2",
    "PORK",
    "ENCHANTED_DIAMOND_BLOCK",
    "EMERALD",
    "ENCHANTED_RABBIT_FOOT",
    "PRISMARINE_CRYSTALS",
    "HOT_POTATO_BOOK",
    "ENCHANTED_ICE",
    "ICE",
    "CLAY_BALL",
    "HUGE_MUSHROOM_1",
    "HUGE_MUSHROOM_2",
    "LOG_2:1",
    "GREEN_GIFT",
    "GOLDEN_TOOTH",
    "STRING",
    "PACKED_ICE",
    "WATER_LILY",
    "RABBIT_FOOT",
    "LOG_2",
    "REDSTONE",
    "ENCHANTED_OBSIDIAN",
    "ENCHANTED_COAL",
    "COAL",
    "ENCHANTED_QUARTZ",
    "ENDER_PEARL",
    "ENCHANTED_COAL_BLOCK",
    "ENCHANTED_CACTUS_GREEN",
    "ENCHANTED_PRISMARINE_CRYSTALS",
    "ENCHANTED_CARROT_ON_A_STICK",
    "ENCHANTED_ENDSTONE",
    "ENCHANTED_LAPIS_LAZULI_BLOCK",
    "ENCHANTED_COOKIE",
    "ENCHANTED_STRING",
    "SLIME_BALL",
    "ENDER_STONE",
    "ENCHANTED_RAW_FISH",
    "ENCHANTED_ACACIA_LOG",
    "ENCHANTED_EGG",
    "QUARTZ",
    "ENCHANTED_EYE_OF_ENDER",
    "SAND",
    "RAW_CHICKEN",
    "MAGMA_CREAM",
    "SUGAR_CANE",
    "ENCHANTED_LAPIS_LAZULI",
    "ENCHANTED_GHAST_TEAR",
    "ENCHANTED_COCOA",
    "RED_GIFT",
    "ENCHANTED_RAW_BEEF",
    "SEEDS",
    "ENCHANTED_LEATHER",
    "ENCHANTED_SPONGE",
    "ENCHANTED_FEATHER",
    "ENCHANTED_SLIME_BLOCK",
    "ENCHANTED_OAK_LOG",
    "RABBIT_HIDE",
    "WHITE_GIFT",
    "INK_SACK",
    "FLINT",
    "ENCHANTED_SPRUCE_LOG",
    "WOLF_TOOTH",
    "ENCHANTED_ROTTEN_FLESH",
    "ENCHANTED_GRILLED_PORK",
    "SULPHUR",
    "NETHER_STALK",
    "RABBIT",
    "ENCHANTED_NETHER_STALK",
    "ENCHANTED_REDSTONE_BLOCK",
    "ENCHANTED_QUARTZ_BLOCK",
    "ENCHANTED_CARROT",
    "ENCHANTED_PUMPKIN",
    "GREEN_CANDY",
    "ENCHANTED_REDSTONE",
    "ROTTEN_FLESH",
    "ENCHANTED_COOKED_FISH",
    "OBSIDIAN",
    "ENCHANTED_MAGMA_CREAM",
    "GRAVEL",
    "MELON",
    "RAW_FISH:3",
    "ENCHANTED_PRISMARINE_SHARD",
    "ENCHANTED_IRON_BLOCK",
    "LEATHER",
    "ENCHANTED_COOKED_MUTTON",
    "BONE",
    "RAW_FISH:1",
    "REVENANT_FLESH",
    "ENCHANTED_PORK",
    "ENCHANTED_GLOWSTONE",
    "ENCHANTED_BREAD",
    "FEATHER",
    "ENCHANTED_CHARCOAL",
    "ENCHANTED_BLAZE_POWDER",
    "NETHERRACK",
    "SUMMONING_EYE",
    "SPONGE",
    "BLAZE_ROD",
    "ENCHANTED_DARK_OAK_LOG",
    "ENCHANTED_BAKED_POTATO",
    "COMPACTOR",
    "ENCHANTED_DIAMOND",
    "ENCHANTED_GOLD"
  ]
        self.iteml = [
            "WHEAT",
            "SEEDS",
            "CARROT_ITEM",
            "POTATO_ITEM",
            "PUMPKIN",
            "MELON",
            "RED_MUSHROOM",
            "BROWN_MUSHROOM",
            "INK_SACK:3",
            "CACTUS",
            "SUGAR_CANE"
  ]
        self.items = []
        self.itemb = []
        counter = len(self.iteml)
        for item in self.iteml:
            url = "https://api.hypixel.net/skyblock/bazaar/product?key=58526953-7fc6-48dc-83a1-78bcfceefaac&productId="+item
            time.sleep(0.5)
            data = requests.get(url).json()
            data = data['product_info']
            data = data['quick_status']
            datb = data['sellPrice']
            self.items.append(datb)
            datb = data['buyPrice']
            self.itemb.append(datb)
            print(counter)
            counter = counter-1
    def udate(self):
        self.items = []
        self.itemb = []
        counter = len(self.itemw)
        for item in self.itemw:
            url = "https://api.hypixel.net/skyblock/bazaar/product?key=58526953-7fc6-48dc-83a1-78bcfceefaac&productId="+item
            time.sleep(0.5)
            data = requests.get(url).json()
            data = data['product_info']
            data = data['quick_status']
            datb = data['sellPrice']
            self.items.append(datb)
            datb = data['buyPrice']
            self.itemb.append(datb)
            print(counter)
            counter = counter-1
    def get_sell_price(self,item):
        #url = "https://api.hypixel.net/skyblock/bazaar/product?key=58526953-7fc6-48dc-83a1-78bcfceefaac&productId="+item
        #data = requests.get(url).json()
        #data = data['product_info']
        #data = data['quick_status']
        #data = data['sellPrice']
        #time.sleep(0.5)
        if item == "null" or item == 'a':
            return 0
        else:
            data = self.items[self.iteml.index(item)]
            return data
    def get_buy_price(self,item):
        #url = "https://api.hypixel.net/skyblock/bazaar/product?key=58526953-7fc6-48dc-83a1-78bcfceefaac&productId="+item
        #data = requests.get(url).json()
        #data = data['product_info']
        #data = data['quick_status']
        #data = data['buyPrice']
        #time.sleep(0.5)
        data = self.itemb[self.iteml.index(item)]
        return data
    def find_best_minion(self):
        prices = []
        counter = len(self.minions)
        for item in self.minions:
            a = self.get_sell_price(item)
            #print(counter)
            counter -= 1
            prices.append(a)
        item_prices = list(zip(prices, self.minions))
        item_prices.sort()
        item_prices.reverse()
        return str(item_prices[:15])
    def update(self):
        print("if you dont know an item, search it up")
        print("The best minion is"+self.find_best_minion())
        
