import os
from Get import getkey

def init():
    x,y = os.get_terminal_size()

def main():
    init()
    print(x,y)

if __name__ == "__main__":
    main()