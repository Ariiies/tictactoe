import pygame, sys, time, random
import Clases.clases as clases
from pygame.constants import QUIT
from pygame.font import SysFont
# Inicialize screen
pygame.init()
HEIGHT, WIDTH =  520, 670
color = pygame.Color(12,106,233)
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
Ref = [[0 for i in range(3)] for n in range(3)]
xpoints, opoints, Mode = 0, 0, False
# function to put elements on the board
def PutTable():
    if not Mode:
        mode = "si"
    else:
        mode="no"
    # point text
    font = pygame.font.SysFont('consolas', 20)
    text = font.render(f" X {xpoints} - {opoints} O", True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.topleft = [HEIGHT/2,30]
    Screen.blit(text, text_rect)
    # text for choice if play alone or not
    font2 = pygame.font.SysFont('consolas', 15)
    text2 = font2.render(f" Play Alone: {mode}", True, (255,255,255))
    text3 = font2.render("Push space for change", True,(255,255,255))
    text2_rect = text2.get_rect()
    text2_rect.topleft = [10,30]
    text3_rect = text3.get_rect()
    text3_rect.topleft = [10,10]
    Screen.blit(text2, text2_rect)
    Screen.blit(text3, text3_rect)
    lineaA.Poner((120,190))
    lineaA.Poner((120,320))
    lineaA.Poner2((240,70))
    lineaA.Poner2((360,70))
    Tablero.draw(Screen)
    pygame.display.flip()
# function for put a temporally message
def TemporalMessage(mensaje="", timer=4, x=335, y=60):
    font = pygame.font.SysFont('Helvetica', 20)
    for n in range(timer,0,-1):
        Screen.fill(color)
        text = font.render(f"{mensaje} restart in {n-1}", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = [x, y]
        Screen.blit(text, text_rect)
        PutTable()
        time.sleep(1)
def GameDraw():
    global Ref
    Draw = False
    for item in Ref:
        for element in item:
            if element == 0:
                Draw = True
    if not Draw:
        TemporalMessage(mensaje="Game Over! it's a Draw")
        for i in range(3):
            for n in range(3):
                Ref[i][n] = 0
        PutTable()
        clases.Turno = True
        Tablero.remove(Tablero)

def Win(A,B,C):
    if (A == "X" and B == "X" and C =="X"):
        return [True, 'X', 0]
    elif (A == "O" and B == "O" and C =="O"):
        return [True, 'O', 0]
    else:
         return [False, 0, 0]

def IsWin():
    global Ref
    W = [False, False, False]
    for n in range(3):
        A = Win(Ref[n][0],Ref[n][1],Ref[n][2])
        if A[0] and n==0:
            W = A
            W[2]=1
        elif A[0] and n==1:
            W = A
            W[2]=2
        elif A[0] and n==2:
            W = A
            W[2]=3
        A = Win(Ref[0][n],Ref[1][n],Ref[2][n])
        if A[0] and n==0:
                W = A
                W[2]=4
        elif A[0] and n==1:
                W = A
                W[2]=5
        elif A[0] and n==2:
                W = A
                W[2]=6
    A = Win(Ref[0][0],Ref[1][1],Ref[2][2])
    if A[0]:
        W = A
        W[2]=7
    A = Win(Ref[0][2],Ref[1][1],Ref[2][0])
    if A[0]:
        W = A
        W[2]=8
    return W

lineaA = clases.Line1(Screen)
Tablero = clases.Table()

# function for gave the coords in X
def PutInX(coord):
    base_x = 140
    incremento_x = 129
    x, r = 0, 0
    if coord > 150 and coord < 250:
            x, r = base_x, 0
    elif coord > 270 and coord <370:
        x, r = base_x+incremento_x, 1
    elif coord > 390 and coord <490:
        x, r = base_x+incremento_x*2, 2
    return (x, r)
# functio for gave the coords in Y
def PutInY(coord):
    base_y = 95
    incremento_y = 130
    y, r = 0, 0
    if coord> 100 and coord< 200:
        y, r= base_y, 0
    elif coord > 220 and coord < 320:
        y, r = base_y+incremento_y, 1
    elif coord > 340 and coord < 440:
        y, r = base_y+incremento_y*2, 2
    return (y, r)
# function for put the victory line in a vertically way
def putWinLine(num):
    for n in range(120):
        PutTable()
        b = clases.WinLine(num,90+(3*n+1))
        Tablero.add(b)
        PutTable()
# function for put the victory line in horizontally way
def putWinLine2(num):
    for n in range(120):
        PutTable()
        b = clases.WinLine(140+(3*n+1),num)
        Tablero.add(b)
        PutTable()
# function to put the victory line in a cross way
def putWinLine3(num):
    if num < 150:
        x=1
    else:
        x=-1
    for n in range(120):
        PutTable()
        b = clases.WinLine(num+x*(3*n),99+(3*n))
        Tablero.add(b)
        PutTable()
# main loop
while True:
    Screen.fill(color)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Mode == False:
                    Mode = True 
                elif Mode == True:
                    Mode = False
    if clases.Turno or Mode:
        if pygame.mouse.get_pressed()[0]:
            print(pygame.mouse.get_pos())
            coords = pygame.mouse.get_pos()
            x = PutInX(coords[0])
            y = PutInY(coords[1])
            if x[0] != 0 and y[0] != 0:
                if Ref[x[1]][y[1]] == 0:
                    Tablero.PonerEquis(x[0], y[0])
                    if not clases.Turno:
                        Ref[x[1]][y[1]]= 'X'
                    else:
                        Ref[x[1]][y[1]]= 'O'
            time.sleep(0.1)
    elif not Mode:
        time.sleep(0.5)
        ran_x = random.randint(0,2)
        ran_y = random.randint(0,2)
        if Ref[ran_x][ran_y] == 0:
            if ran_x == 0:
                pos_x = 175
            elif ran_x == 1:
                pos_x = 275
            elif ran_x == 2:
                pos_x = 400
            if ran_y == 0:
                pos_y = 130
            elif ran_y ==1:
                pos_y = 250
            elif ran_y == 2:
                pos_y = 370
            Ref[ran_x][ran_y] = 'O'
            pos_x = PutInX(pos_x)
            pos_y = PutInY(pos_y)
            Tablero.PonerEquis(pos_x[0], pos_y[0])
    # part for know if someone win
    ganar = IsWin()
    # if someone win, ths part check and put the victory
    if ganar[0]:
            font = pygame.font.SysFont('Helvetica', 20)
            base, incremento = 190, 130
            base2, incremento2 = 145, 100
            if ganar[2] == 1:
                putWinLine(base)
            elif ganar[2]==2:
                putWinLine(base+incremento)
            elif ganar[2]==3:
                putWinLine(base+incremento*2)
            elif ganar[2]==4:
                putWinLine2(base2)
            elif ganar[2]==5:
                putWinLine2(base2+incremento)
            elif ganar[2]==6:
                putWinLine2(base2+incremento*2)
            elif ganar[2]==7:
                putWinLine3(140)
            elif ganar[2]==8:
                putWinLine3(495)
            # show the message for the winner and restart the game
            TemporalMessage(f"Player {ganar[1]} Wins!")
            for i in range(3):
                for n in range(3):
                    Ref[i][n] = 0
            if ganar[1]=="X":
                xpoints+=1
            elif ganar[1]=="O":
                opoints+=1
            Tablero.remove(Tablero)
            clases.Turno = True
    GameDraw()
    PutTable()