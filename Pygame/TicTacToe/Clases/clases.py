import pygame

Turno = True
# classes for the game
# classes for put the lines on the board
patch = r"C:\Users\luisa\projects\03-Tic-Tac-Toe\Pygame\TicTacToe\img/" # my rute for the imgages
class Line1():
    def __init__(self, Screen):
        self.linea1 = pygame.image.load(patch+'LineaNegra1.png')
        self.linea2 = pygame.image.load(patch+'LineaNegra2.png')
        self.Screen = Screen
    def Poner(self,COO):
        self.Screen.blit(self.linea1,COO)
    def Poner2(self,COO):
        self.Screen.blit(self.linea2,COO)
    def Saber(self):
        print (self.linea1)

class WinLine(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        super().__init__()
        self.image = pygame.image.load(patch+'red.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        # movement
        self.speed = [0,0]
class Equis(pygame.sprite.Sprite):
    def __init__(self, Position):
        super().__init__()
        self.image = pygame.image.load(patch+'equis.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Position
        self.speed = [0,0]

class Circulo(pygame.sprite.Sprite):
    def __init__(self, Position):
        super().__init__()
        self.image = pygame.image.load(patch+'circulo.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Position
        self.speed = [0,0]

class Table(pygame.sprite.Group):
    global Turno 
    def __init__(self):
        super().__init__()
        self.pos_x, self.pos_y =  pygame.mouse.get_pos()# 100, 100 
    def PonerEquis(self, x, y):   
        global Turno
        if Turno:
            equis = Equis((x, y))
            self.add(equis)
            Turno = False
        else:
            circulo = Circulo((x, y))
            self.add(circulo)
            Turno = True