from sys import platform
if platform[:3] == 'win':
    import ctypes
    import msvcrt
    
    def getch():
        n = ord(ctypes.c_char(msvcrt.getch()).value)
        try:
            c = chr(n)
        except:
            c = '\0'
        return (n, c)

    def getkey():
        n, c = getch()
        # 0xE0 is 'grey' keys.  change this if you don't like it, but I don't care what color the key is.  IMHO it just confuses the end-user if they need to know.
        if n == 0 or n == 0xE0:
            n, c = getch()
            return "key%x" % n
        return c
    
elif platform[:3] == 'lin' or platform[:3] == 'dar':
    import tty
    import termios
    from sys import stdin
    def getch():
        fd = stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(stdin.fileno())
            ch = stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def getkey():
        getchar = getch
        c1 = getchar()
        if ord(c1) != 0x1b:
            return c1
        c2 = getchar()
        if ord(c2) != 0x5b:
            return c1 + c2
        c3 = getchar()
        if ord(c3) != 0x33:
            return c1 + c2 + c3
        c4 = getchar()
        return c1 + c2 + c3 + c4
