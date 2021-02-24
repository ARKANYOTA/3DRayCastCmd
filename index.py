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

########
# Main #
########
def main():
    """Main"""
    # Init
    ## Terminal size
    size = x_size, y_size = os.get_terminal_size()

    # Boucle infini
    while 1:
        ## Getkey as key
        key = getkey()
        print(key)
        clear_screen()
        draw_pixel(10,10,"X")
        draw_rect(10,10,20,20,":")
        draw_rect(25,25,33,33,fill=False)

if __name__ == "__main__":
    main()