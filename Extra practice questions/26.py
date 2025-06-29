# # 4-5. Summing a Million: Make a list of the numbers from one to one
# million, and then use min() and max() to make sure your list actually starts at
# one and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.
# Create a list of numbers from 1 to 1,000,000
numbers = list(range(1,1000001))

# Use min(), max(), and sum()
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of all numbers:", sum(numbers))