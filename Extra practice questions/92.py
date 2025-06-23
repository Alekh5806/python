print("Why do you like programming?")
print("Type 'q' to quit.\n")

while True:
    reason = input("Your reason: ")
    if reason.lower() == 'q':
        break
    with open("programming_poll.txt", "a") as file:
        file.write(f"{reason}\n")
    print("Thank you! Your response has been recorded.\n")