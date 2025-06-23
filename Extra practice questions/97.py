filename = '/Users/alekh/Desktop/python/Extra practice questions/alice.txt'  

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    word_count = contents.lower().count('the')
    print(f"The word 'the' appears about {word_count} times in {filename}.")