filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            contents = file.read()
            print(contents.strip())
    except FileNotFoundError:
        print(f"\n⚠️ The file '{filename}' was not found.")