def opener(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def converter(string):
    l = list(string.split(' '))
    return l

def counter(l):
    res=0
    for i in range(len(l)):
        res+=len(l[i].split())
    print(l)
    print('Number of words: '+str(res))

def main():
    string = input("Input file name or text you want to count words in: ")
    try:
        l = opener(string)
        counter(l)
    except:
        l = converter(string)
        counter(l)

main()