# 4-13. Buﬀet: A buﬀet-style restaurant oﬀers only five basic foods. Think of
# five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant oﬀers.
# Try to modify one of the items, and make sure that Python rejects the
# change.
# The restaurant changes its menu, replacing two of the items with diﬀerent
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

simple_food = ("roti","chaval","sabji","chole","chaas")
for food in simple_food:
  print(f"the restaurant offers : {food}")

# simple_food(1)="papad"
# print(simple_food)

new_menu = ("roti","sbaji","papad","chole","raita")
for food in new_menu:
  print(f"the new menu is : {food}")