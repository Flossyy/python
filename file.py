
def ifInteger(value):
    if value.strip().isdigit(): return True
    else: return False

def main():
    val=input("What number are you thinking about:")
    if ifInteger(val) :
        if int(val) % 2==0:
            (print("This number is even!")) 
        else:
            (print("This number is odd!"))
    else: 
        print("Not a integer :/")
    loop=True
    while(loop):
        val=input("Have another? If no input 0:")
        if ifInteger(val) :
            if int(val) == 0:break
            if int(val) % 2==0:
                (print("This number is even!")) 
            else:
                (print("This number is odd!"))
        else: 
            print("Not a integer :/")
main()
            