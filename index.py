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

########
# Main #
########
def main():
    """Main"""
    # Init
    ## Terminal size
    size = x_size, y_size = os.get_terminal_size()
    map = """22222222
20000002
20000002
20000002
20000002
20000002
20000002
22222222"""
    ShowMap = False

    # Boucle infini
    while 1:
        ## Getkey as key
        key = getkey()
        print(key)
        if key=="m":
            ShowMap= not (ShowMap)
        clear_screen()
        draw_pixel(10,10,"X")
        draw_rect(10,10,20,20,":")
        draw_rect(25,25,33,33,fill=False)
        draw_1px_line(7,2, 10, char="!", vertical=False)
        draw_1px_line(9,7, 10, char="^")
        if ShowMap:
            print("\033[1;1H"+map)

if __name__ == "__main__":
    main()