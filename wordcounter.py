def opener():
    with open('README.md') as f:
        lines = f.readlines()
    return lines

def counter():
    res=0
    list = opener()
    for i in range(len(list)):
        res+=len(list[i].split())
    print(list)
    print("Number of words: "+str(res))

def main():


main()