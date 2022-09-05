def make_shirt(size, message):
    """ param: size and message of the shirt, then sum up the order"""
    print(f"The shirt size you have ordered is: {size}\n and the custom masseg({message}) will be printed..\n thank you for ordering..")
    pass


make_shirt(input("your size please:\t"), input("any custom message you would like:\t"))
# that was the positional argument

print("-"*50)

make_shirt(size=input("please provide us with your size::"), message=str(input("if you would like to add a custom message::")))
# this is the keyword argument...
