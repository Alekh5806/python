# Write a program to generate multiplication table from 2 to 20 and write it to the different files.Place these files in a folder for a 13 - year old child.

# this function stores the table in various files 
def genrateTable(n):
  table=""
  for i in range(1,11):
    table += f"{n} * {i} = {n*i}\n"
  
  with open(f"/Users/alekh/Desktop/python/ch-09/tables/table_{n}.txt","w") as f:
    f.write(table)


# calling the function yo make the table from 2 to 20
for i in range(2,21):
  genrateTable(i)