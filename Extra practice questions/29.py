# 4-8. Cubes: A number raised to the third power is called a cube. For
# example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10
# cubes (that is, the cube of each integer from 1 through 10), and use a for
# loop to print out the value of each cube
# Step 1: Create a list of numbers from 1 to 10
cubes = list(range(1, 11))
print(f"Numbers to be cubed: {cubes}")

final_cubes = []


for number in cubes:
    print(number**3)               
    final_cubes.append(number**3)

print(f"\nFinal list of cubes: {final_cubes}")