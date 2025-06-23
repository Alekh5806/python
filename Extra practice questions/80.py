class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create 3 instances
restaurant1 = Restaurant("Tandoori Treats", "Indian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Bella Italia", "Italian")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()