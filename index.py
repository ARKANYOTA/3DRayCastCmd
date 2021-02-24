import os
from get import getkey as gk
def getkey():
    key = gk()
    if key=="\x03":
        exit()
    else:
        return key   

def main():
    x,y = os.get_terminal_size()
    print(x,y)
    while 1:
        key = getkey()
        print(key)

if __name__ == "__main__":
    main()