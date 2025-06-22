#2-8. File Extensions: Python has a removesuffix() method that worksexactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename_extension = "python_notes.txt"
filename = filename_extension.removesuffix('.txt')
print(f"file name is {filename}")