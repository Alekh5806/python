# 3-6. More Guests: You just found a bigger dinner table, so now more space
# is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.


# Original guest list
guest_list = ["Albert Einstein", "APJ Abdul Kalam", "Elon Musk"]

# Print original invitations
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

# Announce the guest who can't make it
unable_to_attend = "APJ Abdul Kalam"
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")

# Replace the guest who can't make it
guest_list[guest_list.index(unable_to_attend)] = "Nikola Tesla"

print("Great news! We found a bigger dinner table, so we can invite more guests.\n")

# Add new guests
guest_list.insert(0, "Marie Curie")                   # Add at the beginning
guest_list.insert(len(guest_list) // 2, "Ada Lovelace")  # Add in the middle
guest_list.append("Isaac Newton")                    # Add at the end

# Print updated invitations
for guest in guest_list:
    print(f"Dear {guest}, you’re invited to dinner at my place. Looking forward to your presence!")

