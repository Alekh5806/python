# Base class
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")

# Subclass: Admin
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nAdmin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Create Admin instance
admin_user = Admin("krunal", "goswami")

# Call methods
admin_user.describe_user()
admin_user.show_privileges()