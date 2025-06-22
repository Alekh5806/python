# 3-7. Shrinking Guest List: You just found out that your new dinner table
# won't arrive in time for the dinner, and now you have space for only two
# guests.
# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you're sorry you can't invite
# them to dinner.
# Print a message to each of the two people still on your list, letting them
# know they're still invited.
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.


# Guest list from Exercise 3-6
guest_list = ["Marie Curie", "Albert Einstein", "Ada Lovelace", "Nikola Tesla", "Elon Musk", "Isaac Newton"]

# Announce the bad news
print("Bad news! The new dinner table won't arrive in time, so I can invite only two people.\n")

# Remove guests until only two remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner this time.")

# Invite the remaining two guests
print("\nGood news:")
for guest in guest_list:
    print(f"{guest}, you're still invited to dinner!")

# Remove the last two guests from the list
del guest_list[0]
del guest_list[0]

# Confirm the list is now empty
print("\nFinal guest list (should be empty):", guest_list)

