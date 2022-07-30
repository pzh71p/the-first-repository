class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = number

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"We provides wonderful {self.cuisine_type.title()} !")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open!")

    def set_number_served(self):
        print(f"We have served {self.number} people!")

    def increment_number_served(self, increment):
        if increment < 0:
            print("You can't have roll back number of people!")
        else:
            print(f"We have served {self.number} people until yesterday!")
            self.number += increment
            print(f"We have served {increment} people today!")
            print(f"Until today we have served {self.number} people!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, number=0):
        super().__init__(restaurant_name, cuisine_type, number=0)
        self.flavours = [ ]

    def show_flavours(self):
        print(f"We have a a variety of {self.cuisine_type.title()} such as : ")
        for i in self.flavours:
            print(f"\t{i.title()} ice cream")


base = ["strawberry", "matcha", "raspberry", "blueberry", "vanilla"]
my_ice = IceCreamStand('warm cabin', 'ice cream', 332)
my_ice.flavours = base
my_ice.show_flavours()

my_restaurant = Restaurant('chinese restaurant', 'chinese food', 334)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(32)
