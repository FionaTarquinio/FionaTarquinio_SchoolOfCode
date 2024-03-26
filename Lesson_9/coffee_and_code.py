class KitchenAppliance:
        
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):

    def __init__(self, model_number, brand, coffee_menu = []):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, coffee_type):
        if coffee_type not in self.coffee_menu:
            self.coffee_menu.append(coffee_type)
            print(f"'{coffee_type}' has been added to the menu of your smart machine.\n")
        else:
            print(f"'{coffee_type}' is already on the menu of your smart machine.\n")
        
    def make_coffee(self, coffee_type):
        while (coffee_type not in self.coffee_menu):
            print(f"'{coffee_type}' is not on the menu of your smart machine.\nWould you like to add it to the menu? (y/n):\n")
            if input().lower() == "y":
                my_machine.update_menu(coffee_type)
            
            print("Please select your coffee from the following menu options:")  
            for item in self.coffee_menu:
                print(item)
            coffee_type = input()    
        
        print(f"Now making your {coffee_type}...")    

my_machine = SmartCoffeeMachine(1800, "Smeg", ["cafe latte", "cappuccino", "long black"])

my_machine.report()

my_machine.update_menu(input(f"Enter the coffee type you would like to add to the menu of your {my_machine.brand} {my_machine.model_number}:\n"))

my_machine.make_coffee(input("Select coffee type:\n"))


