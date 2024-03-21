class SmartDevice:
    def __init__(self, model_number, brand, screen_size, app_list = []):
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print(f"This is {self.model_number} from {self.brand}")

    def install_app(self, app_name = "Demo App"):
        print(f"Installing {app_name}...")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
            return self.app_list
        else:
            print(f"{app_name} already installed.")

    def delete_app(self, app_name = "Demo App"):
        app_name = input("Which app would you like to delete?:\n")
        if app_name in self.app_list:
            self.app_list.remove(app_name)
            print(f"{app_name} removed.")
        else:
            print(f"{app_name} is not installed on your device.")

device_a = SmartDevice(1233244, "CLG", 5.7)
device_a.report()
print(device_a.install_app("Python Dojo"))
device_a.install_app()
print(device_a.app_list)
device_a.install_app()
print(device_a.app_list)
device_a.delete_app()
print(device_a.app_list)