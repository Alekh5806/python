# 3-10. Every Function: Think of things you could store in a list. For
# example, you could make a list of mountains, rivers, countries, cities,
# languages, or anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this
# chapter at least once.


# Create a list of cities
cities = ["Tokyo", "Paris", "New York", "Rio de Janeiro", "Sydney"]

# 1. Print original list
print("Original list:")
print(cities)

# 2. Access elements by index
print("\nFirst city in the list:")
print(cities[0])

# 3. Use title() method
print("\nSecond city with title case:")
print(cities[1].title())

# 4. Modify an element
cities[2] = "London"
print("\nChanged 'New York' to 'London':")
print(cities)

# 5. Add a new element with append()
cities.append("Dubai")
print("\nAdded 'Dubai' using append():")
print(cities)

# 6. Insert an element at a specific position
cities.insert(2, "Rome")
print("\nInserted 'Rome' at index 2:")
print(cities)

# 7. Delete an item using del
del cities[3]
print("\nDeleted the city at index 3:")
print(cities)

# 8. Remove the last item using pop()
popped_city = cities.pop()
print(f"\nPopped the last city: {popped_city}")
print("List after popping:")
print(cities)

# 9. Remove a specific item by value
cities.remove("Rome")
print("\nRemoved 'Rome' by value:")
print(cities)

# 10. Sort the list temporarily using sorted()
print("\nTemporarily sorted list:")
print(sorted(cities))

# 11. Show original list is unchanged
print("\nOriginal list after sorted():")
print(cities)

# 12. Sort the list permanently
cities.sort()
print("\nList after sort():")
print(cities)

# 13. Reverse the list
cities.reverse()
print("\nList after reverse():")
print(cities)

# 14. Use len() to count elements
print(f"\nNumber of cities in the list: {len(cities)}")