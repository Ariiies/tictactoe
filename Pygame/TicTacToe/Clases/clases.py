import pygame

Turno = True
# classes for the game
# classes for put the lines on the board
class Line1():
    def __init__(self, Screen):
        self.linea1 = pygame.image.load(r'C:\Users\luisa\OneDrive\Escritorio\Web\14-Master Python\07-PyGame\TicTacToe/img/LineaNegra1.png')
        self.linea2 = pygame.image.load(r'C:\Users\luisa\OneDrive\Escritorio\Web\14-Master Python\07-PyGame\TicTacToe/img/LineaNegra2.png')
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
        self.image = pygame.image.load(r'C:\Users\luisa\OneDrive\Escritorio\Web\14-Master Python\07-PyGame\TicTacToe/img/red.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        # movement
        self.speed = [0,0]
class Equis(pygame.sprite.Sprite):
    def __init__(self, Position):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\luisa\OneDrive\Escritorio\Web\14-Master Python\07-PyGame\TicTacToe/img/equis.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = Position
        self.speed = [0,0]

class Circulo(pygame.sprite.Sprite):
    def __init__(self, Position):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\luisa\OneDrive\Escritorio\Web\14-Master Python\07-PyGame\TicTacToe/img/circulo.png')
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