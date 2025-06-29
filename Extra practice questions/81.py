class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")

# Create a user instance
user1 = User("Alekh", "Patel")

# Call methods
user1.describe_user()
user1.greet_user()