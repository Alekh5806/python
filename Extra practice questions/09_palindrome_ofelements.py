# Original list
original_list = [1, "abc", "abc", 1]

# Make a copy of the list
copied_list = original_list.copy()

# Reverse the copied list
copied_list.reverse()

# Check if original and reversed lists are the same
if original_list == copied_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")