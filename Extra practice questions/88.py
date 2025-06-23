# Method 1: Read entire content
with open('/Users/alekh/Desktop/python/Extra practice questions/learning_python.txt') as file:
    contents = file.read()
    print("=== Entire File ===")
    print(contents)

# Method 2: Read line by line
print("\n=== Line by Line ===")
with open('/Users/alekh/Desktop/python/Extra practice questions/learning_python.txt') as file:
    for line in file:
        print(line.strip())

# Method 3: Store lines in a list
print("\n=== From List ===")
with open('/Users/alekh/Desktop/python/Extra practice questions/learning_python.txt') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())