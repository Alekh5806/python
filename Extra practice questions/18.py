# 3-8. Seeing the World: Think of at least five places in the world you’d like
# to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse-alphabetical order without changing
# the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s
# back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.



# List of places I want to visit
places = ["Japan", "Iceland", "New Zealand", "Switzerland", "Brazil"]

# Original order
print("Original list:")
print(places)

# Alphabetical order (without modifying the original list)
print("\nSorted list (alphabetical):")
print(sorted(places))

# Show that original list is still unchanged
print("\nOriginal list after sorted():")
print(places)

# Reverse alphabetical order (without modifying the original list)
print("\nSorted list (reverse alphabetical):")
print(sorted(places, reverse=True))

# Show that original list is still unchanged
print("\nOriginal list after reverse sorted():")
print(places)

# Reverse the order of the list (modifies the list)
places.reverse()
print("\nList after reverse():")
print(places)

# Reverse again to get original order back
places.reverse()
print("\nList after second reverse() (original order restored):")
print(places)

# Sort the list alphabetically (modifies the list)
places.sort()
print("\nList after sort() (alphabetical):")
print(places)

# Sort the list in reverse alphabetical order (modifies the list)
places.sort(reverse=True)
print("\nList after sort(reverse=True) (reverse alphabetical):")
print(places)
