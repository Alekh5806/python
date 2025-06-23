# Parent class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Child class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mango']

    def display_flavors(self):
        print(f"\n{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Create an instance
ice_cream_shop = IceCreamStand("Cool Cones")

# Call methods
ice_cream_shop.describe_restaurant()
ice_cream_shop.display_flavors()