# Replace "Python" with "C" in each line from the file
print("=== Replacing 'Python' with 'C' ===")
with open('/Users/alekh/Desktop/python/Extra practice questions/learning_python.txt') as file:
    for line in file:
        modified_line = line.replace("Python", "C")
        print(modified_line.strip())