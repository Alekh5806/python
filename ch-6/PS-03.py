# A spam comment is defined as a text containing following keywords: "make a lot of money","buy now","subscribe this","click this".Write a program to detect this.
spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

message = input("enter the message: ")
# We will here use the "in" keyword
if((spam1 in message) or (spam2 in message) or (spam3 in message) or (spam4 in message)):
  print("this msg is a spam msg you can ignore it...")
else:
  print("this is not a spam msg plz read it....")