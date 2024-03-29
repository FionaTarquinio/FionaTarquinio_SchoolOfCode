class KitchenAppliance:
        
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    
    def report(self):
        print("This is the " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):

    def __init__(self, model_number, brand, coffee_menu = []):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, coffee_type):
        if coffee_type.lower() not in self.coffee_menu:
            self.coffee_menu.append(coffee_type.lower())
            print(f"'{coffee_type.lower()}' has been added to the menu of your {self.brand} {self.model_number}.\n")
        else:
            print(f"'{coffee_type.lower()}' is already on the menu of your {self.brand} {self.model_number}.\n")
        
    def make_coffee(self, coffee_type):
        while (coffee_type.lower() not in self.coffee_menu):
            print(f"'{coffee_type.lower()}' is not on the menu of your {self.brand} {self.model_number}.\nWould you like to add it to the menu? (y/n):\n")
            if input().lower() == "y":
                my_machine.update_menu(coffee_type.lower())
            
            print("Please select your coffee from the following menu options:")  
            for item in self.coffee_menu:
                print(item)
            coffee_type = input().lower()    
        
        print(f"Now making your {coffee_type}...")    

my_machine = SmartCoffeeMachine(1800, "Smeg", ["cafe latte", "cappuccino", "long black"])

my_machine.report()

my_machine.update_menu(input(f"Enter the coffee type you would like to add to the menu of your {my_machine.brand} {my_machine.model_number}:\n"))

my_machine.make_coffee(input("Select coffee type:\n"))


