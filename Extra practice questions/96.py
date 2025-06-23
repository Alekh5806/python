filenames = ['cats.txt', 'dogs.txt', 'parrots.txt']  # parrots.txt doesn't exist

for filename in filenames:
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            contents = file.read()
            print(contents.strip())
    except FileNotFoundError:
        pass  # Silent fail — do nothing if file is missing