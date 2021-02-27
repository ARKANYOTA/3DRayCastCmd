###############
# Importation #
###############
import os
from get import getkey as gk
import math
import numpy as np

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


def get_ray_lenth(angle, map_, player_x, player_y):
    """angle: int en radient, map_: ..., player_x et player_y: float"""
    dec_x = player_x % 1
    dec_y = player_y % 1
    if 90 < angle < 270:
        delta_x = dec_x 
    else:
        delta_x = 1-dec_x 
    if 0 <= angle < 180:
        delta_y = dec_y 
    else:
        delta_y = 1-dec_y
    tang = delta_y/delta_x
    longeur = 2
    print(f"player(x,y): ({player_x}, {player_y})||angle: {angle} ||delta_x: {delta_x}||delta_y: {delta_y}")
    return longeur

def get_ray_x_lenth(angle, map_, player_x, player_y):
    # cos(ang) = adj/hyp
    # hyp = adj/cos(ang)
    angle = angle % 360
    dec_x = player_x % 1
    if 90 < angle < 270:
        delta_x = dec_x 
    else:
        delta_x = 1-dec_x
    if 90 < angle < 180 or 270 < angle < 360:
        cosangle = 90 - (angle%90)
    elif angle==90 or angle==270:
        if angle==90:
            return round(player_y % 1,4)    # division par 0 car cos(90)=0
        if angle==270:
            return round(1-(player_y % 1),4)    # division par 0 car cos(270)=0
    else:
        cosangle = (angle%90)
    
    longeur = delta_x/ math.cos(math.radians(cosangle))
    return round(longeur,4)
#   X 
#   |\           |    return du longeur entre y(PlaYer) et le X
#   | \          |
#-- |--\---------------
#   |   \        |
#   |    \       |
#   |     \      |
#   |   Player   |
#   |            |
#-- |------------------
def get_ray_y_lenth(angle, map_, player_x, player_y): # Pas ce fier a ce calcul: l'autre est meiux
    # cos(ang) = adj/hyp
    angle = angle % 360
    dec_y = player_y % 1
    if 90 < angle < 270:
        delta_y = 1-dec_y
    else:
        delta_y = dec_y
    if 0 < angle < 90 or 180 < angle < 270:
        cosangle = 90 - (angle%90)
    elif angle==180 or angle==0:
        if angle==180:
            return round(player_x % 1,4)    # division par 0 car cos(90)=0
        if angle==0:
            return round(1-(player_x % 1),4)    # division par 0 car cos(270)=0
    else:
        cosangle = (angle%90)
    
    longeur = delta_y/ math.cos(math.radians(cosangle))
    return round(longeur,4)

def nombre_de_lenth(angle, map_, player_x, player_y):
    # tan(angle) = coef/1
    # coef = tan(angle) * 1 = tan(angle)
    nombre_de_block = 6
    coef_directeur = math.tan(math.radians(angle))
    return round(angle,4), round(coef_directeur, 4) ,nombre_de_block


def afficher_les_longeur(x_size, y_size, map_, player_x, player_y, FOV, angle):
    angle_d_un_pixel = FOV/x_size
    # list_of_range_number = [k for k in range(int(angle), int(angle+FOV))]
    # list_of_angles = [k*angle_d_un_pixel for k in list_of_range_number]
    for x in np.arange(int(angle), int(angle+FOV), angle_d_un_pixel):
        print(nombre_de_lenth(x, map_, player_x, player_y))

########
# Main #
########
def main():
    """Main"""
    # Init
    ## Terminal size
    FOV = 90
    size = x_size, y_size = os.get_terminal_size()
    player = player_x, player_y = 2.4, 2.7
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
        afficher_les_longeur(x_size, y_size, map_, player_x, player_y, FOV, 0)
        if ShowMap:
            print_map(map_, x_size, y_size, map_size, tileset=tileset,pos="ru")
        ## Getkey as key
        key = getkey()
        print(key)
        clear_screen()


if __name__ == "__main__":
    main()