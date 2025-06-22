# 3-5. Changing Guest List: You just heard that one of your guests can’t
# make the dinner, so you need to send out a new set of invitations. You’ll
# have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in
# your list.

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

# Print new set of invitations
print("\nNew invitation list:")
for guest in guest_list:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")