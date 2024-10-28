print("LA 22")
class Bday:
    def __init__(self, theme, foods, special_dish, ):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
        
    def print_foods(self): 
        print(f"theme: {self.theme}")
        print(f"foods:")
        print(f"{self.foods['main']}")
        print(f"{self.foods['dessert']}")
        print(f"{self.foods['snack']}")
        print(f"special_dish: {self.special_dish}")
        
    def special_dish(self):
        print(f"special dish: {self.special_dish}")
    
theme_1 = Bday("cubao", {"main": "sopas", "dessert": "spaggeti", "snack": "pansit"}, "salad")
theme_2 = Bday("quiapo", {"main": "lechon", "dessert": "adobo", "snack": "caldereta"}, "crispy pata")
theme_3 = Bday("marikina", {"main": "talong", "dessert": "kalabasa", "snack": "sitaw"}, "bayabas")
theme_1.print_foods()
theme_2.print_foods()
theme_3.print_foods() 