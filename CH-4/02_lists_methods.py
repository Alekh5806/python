names = ["Alekh","Harsh","dirgh","taksh","rahil","krunal",101,3.14,True,False]
#INDEXES- 0        1       2       3       4      5        6    7    8   9
print(names)
names.append("alekh")
print(names)
# List methods manually (no loop used)
print("append - Adds an element to the end")
print("extend - Adds elements of an iterable")
print("insert - Inserts element at given position")
print("remove - Removes first matching element")
print("pop - Removes element at given position")
print("clear - Removes all elements")
print("index - Finds the first index of a value")
print("count - Counts occurrences of a value")
print("sort - Sorts the list")
print("reverse - Reverses the list")
print("copy - Returns a shallow copy")

# code of all methods with example


# Create a sample list
names = ["Alekh","Harsh","dirgh","taksh","rahil","krunal",101,3.14,True,False]

# append() – Adds an element at the end
names.append(50)
print("After append(50):", names)  # [10, 20, 30, 20, 40, 50]

# extend() – Adds elements from another list
names.extend([60, 70])
print("After extend([60, 70]):", names)  # [10, 20, 30, 20, 40, 50, 60, 70]

# insert() – Inserts an element at a specific position
names.insert(2, 25)
print("After insert(2, 25):", names)  # [10, 20, 25, 30, 20, 40, 50, 60, 70]



# pop() – Removes and returns element at given index (default last)
popped_value = names.pop()
print("After pop():", names)  # Last element removed
print("Popped value:", popped_value)

# clear() – Removes all elements from the list
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear():", temp_list)  # []

# index() – Returns index of first matching value
index_value = names.index(30)
print("Index of 30:", index_value)

# count() – Counts how many times a value appears
count_20 = names.count(20)
print("Count of 20:", count_20)

# sort() – Sorts the list in ascending order
unsorted_list = [5, 2, 9, 1]
unsorted_list.sort()
print("After sort():", unsorted_list)  # [1, 2, 5, 9]

# reverse() – Reverses the list
unsorted_list.reverse()
print("After reverse():", unsorted_list)  # [9, 5, 2, 1]

# copy() – Returns a shallow copy of the list
copied_list = names.copy()
print("Copied list:", copied_list)