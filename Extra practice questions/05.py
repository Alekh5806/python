#2-7. Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.Make sure you use each character combination, "\t" and "\n", at least once.
#Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(),rstrip(), and strip().


# Name with whitespace, tabs, and newlines
name = "\t\n  Alekh Patel  \n\t"

# Print with whitespace visible
print("Original name with whitespace:")
print(repr(name))  # Shows special characters like \t and \n

# Print using .strip()
print("\nAfter strip():")
print(repr(name.strip()))

# Print using .lstrip()
print("\nAfter lstrip():")
print(repr(name.lstrip()))

# Print using .rstrip()
print("\nAfter rstrip():")
print(repr(name.rstrip()))