import random 
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("plz enter the lower number..")
        guesses += 1
    elif(a<n):
        print("plz enter the higher number..")
        guesses += 1

print(f"You have guessed the number {n} in {guesses} attempts")