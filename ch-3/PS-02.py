# write a program to fill in a letter tempelate given below with name and date
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
print(letter.replace("<|Name|>","Alekh").replace("<|Date|>","12 June 2025"))