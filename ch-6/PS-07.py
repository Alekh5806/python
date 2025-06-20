# Write a program to find out whether a given post is talking about "Harry" or not.
post = input("Enter the post: ")

if("harry" in post.lower()):  # using lower() we can use input in all form so that it will give the output  
    print("This post is talking about harry")

else:
    print("This post is not talking about harry")