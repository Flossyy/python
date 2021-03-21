val=input("What number are you thinking about:")
try:
    if int(val) % 2==0:
        (print("This number is even!")) 
    else:
        (print("This number is odd!"))
except:
    print("Not a number :/")