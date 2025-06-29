class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Create a user
user1 = User("krunal", "goswami")

# Simulate login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"\nLogin attempts: {user1.login_attempts}")

# Reset attempts
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")