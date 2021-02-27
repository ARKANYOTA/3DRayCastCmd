###############
# Importation #
###############
import os
from get import getkey as gk

#############
# Fonctions #
#############
def getkey():
    """attribut: None, return String, exit si Control+C"""
    key = gk()
    if key=="\x03":  # Ctrl+C
        exit()
    else:
        return key

def draw_pixel(x,y,string="X"):
    """x,y: int ou str, string: string"""
    print("\033[{0};{1}H{2}".format(x,y,string))

def draw_rect(x,y,x_1,y_1, char="X", fill=True):
    """x,y,x_1,x2: int, <char>: String de 1 char(X), <fill>: Boolean (True)"""
    if fill:
        for v in range(x,x_1):
            for h in range(y,y_1):
                draw_pixel(v,h, char)
    else:
        for h in range(y,y_1):
            draw_pixel(x,h, char)
        for h in range(y,y_1):
            draw_pixel(x_1,h, char)
        for v in range(x+1,x_1):
            draw_pixel(v,y, char)
            draw_pixel(v,y_1-1, char)

def clear_screen():
    print("\033[2J")

def draw_1px_line(x,y, size, char="X", vertical=True):
    """x,y: int, <char>: String de 1 char(X), <vertical>: Boolean (True)"""
    if vertical:
        for h in range(size):
            draw_pixel(x+h,y, char)
    else:
        draw_pixel(x,y, string=char*size)

def print_map(map_, size_x, size_y, size_map, tileset, pos="ru", border=True):
    """map: list of list of int, <pos>: [rl][ud] (ru), <border>: bool (True)"""
    if pos[0]=="r":
        y=size_x-size_map+1
    else:
        y=1
    if pos[1]=="d":
        x=size_y-size_map
    else:
        x=1
    for h in range(len(map_)):
        set_pos(x+h, y)
        for v in map_[h]:
            print(tileset[v],end="")
        print()


def set_pos(x,y, printing=True):
    """x,y: int, <printng>: Boolean (True)"""
    if printing:
        print(f"\033[{x};{y}H", end="")
    else:
        return f"\033[{x};{y}H"


########
# Main #
########
def main():
    """Main"""
    # Init
    ## Terminal size
    size = x_size, y_size = os.get_terminal_size()
    player = player_x, player_y = 2.0, 2.0
    map_ = [  # 0: Vide, 1: Mur
            [1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,1],
            [1,0,0,0,1,0,0,1],
            [1,1,0,1,1,1,0,1],
            [1,0,0,1,0,0,0,1],
            [1,0,1,1,0,1,1,1],
            [1,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1]
    ]
    map_size = 8
    ShowMap = False
    key = "init"
    tileset = (" ", "█")

    clear_screen()
    # Boucle infinie
    while 1:
        ### Key Detection
        if key=="m":
            ShowMap= not (ShowMap)
        ## Show screen

        if ShowMap:
            print_map(map_, x_size, y_size, map_size, tileset=tileset,pos="ru")
        ## Getkey as key
        key = getkey()
        print(key)
        clear_screen()


if __name__ == "__main__":
    main()