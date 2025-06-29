class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.\n")

# Create multiple user instances
user1 = User("krunal", "goswami")
user2 = User("alekh", "patel")
user3 = User("riya", "shah")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()