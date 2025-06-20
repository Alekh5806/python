 # We all have played snake, water gun game in our childhood.If you haven't google the rules of this game and write a python program capable of playing this game eith the user 
'''
1 FOR SNAKE
-1 FOR WATER
0 FOR GUN

'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youdict = {'s':1,'w':-1,'g':0}
reverseDict = {1 : "Snake",-1 : "Water",0 : "Gun"}
you = youdict[youstr]

print(f"Ypu choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
  print("it's a draw")
else:
  if(computer == -1 and you == 1):
    print("you win!")
  elif(computer == -1 and you == 0):
    print("You loose!")
  elif(computer == 1 and you == -1):
    print("You loose!")
  elif(computer == 1 and you == 0):
    print("You win!")
  elif(computer == 0 and you == -1):
    print("You win!")
  elif(computer == 0 and you == 1):
    print("You loose!")
  else:
    print("Something went wrong plz try again later....")