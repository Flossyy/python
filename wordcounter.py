def opener():
    with open('README.md') as f:
        lines = f.readlines()
        for i in range(len(lines)): print(lines[i])

def main():
    opener()

main()