# # 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

# Store multiples of 3 in a list
multiples_of_3 = list(range(3, 31, 3))

# Print the full list in one line
print("Full list of multiples of 3 from 3 to 30:")
print(multiples_of_3)

# Print each number individually using a loop
print("\nMultiples printed one by one:")
for number in multiples_of_3:
    print(number)