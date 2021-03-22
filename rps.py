import random
rock = 'rock'
paper = 'paper'
scisors = 'scisors'
def rand():
    number = random.randint(0,2)
    if number == 0 : return rock
    if number == 1 : return paper
    if number == 2 : return scisors

def rpc(player,ai):
    print(player+" vs "+ai)
    if player == ai: 
        save('draw')
        return('draw')
    if player == rock and ai == scisors or player == paper and ai == rock or player == scisors and ai == paper : 
        save('win')
        return('win')
    else : 
        save('lose')
        return('lose') 

def save(score):
    with open('dane.txt','a') as f:
        f.write(score+"\n")
    f.close()

def main():
    while(True):
        val = input('(exit with 0)\nRock, paper or scisors?:')
        randVal = rand()
        try:
            if val == rock or val == paper or val == scisors : print(rpc(val,randVal))
            elif int(val) == 0 : return(0)
        except:
            print("Error")

if __name__ == "__main__":
    main()