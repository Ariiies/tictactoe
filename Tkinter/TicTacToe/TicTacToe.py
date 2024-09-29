from tkinter import *
from tkinter import messagebox

# Main Window
MainWindow = Tk()
MainWindow.title("Tic Tac Toe")
MainWindow.geometry("500x400")
MainWindow.resizable(0,0)
# variables
winsX =0
winsO = 0
Game = [[0 for i in range(3)] for n in range(3)]
turn = 0
space = True
# labels
Wins_Label = Label(MainWindow, text="Wins:").place(x=10, y=10)
X = Label(MainWindow, text=f"X = {winsX}")
X.place(x=10, y=30)
O = Label(MainWindow, text=f"O= {winsO}")
O.place(x=10, y=50)
# Tablero
canvas = Canvas(width=300, height=300, bg='white')
canvas.place(x=100, y=40)
canvas.create_line(100, 0, 100, 300, fill='black', tag= 'tablero')
canvas.create_line(200, 0, 200, 300, fill="black", tag= 'tablero')
canvas.create_line(0, 100, 300, 100, fill='black', tag= 'tablero')
canvas.create_line(0, 200, 300, 200, fill="black", tag= 'tablero')
# Function to click event to put signs in the board
def ClickCanvas(event):
    global turn
    # first block
    if event.x < 100 and event.y < 100 and Game[0][0]==0:
        if turn == 1:
            canvas.create_line(10, 10, 90, 90, width=5, fill="black", tag='equis')
            canvas.create_line(90, 10, 10, 90, width=5, fill="black", tag='equis')
            Game[0][0]=1
            turn = 0
        else:
            canvas.create_oval(10, 10, 90, 90, width=5, fill='white', tag='circulo') 
            Game[0][0]=-1
            turn = 1
    if event.x > 100 and event.x < 200 and event.y < 100 and Game[0][1]==0:
        if turn == 1:
            canvas.create_line(110, 10, 190, 90, width=5, fill="black", tag='equis')
            canvas.create_line(190, 10, 110, 90, width=5, fill="black", tag='equis')
            Game[0][1]=1
            turn = 0
        else:
            canvas.create_oval(110, 10, 190, 90, width=5, fill='white', tag='circulo') 
            Game[0][1]=-1
            turn = 1
    if event.x > 200 and event.y < 100 and Game[0][2]==0:
        if turn == 1:
            canvas.create_line(210, 10, 290, 90, width=5, fill="black", tag='equis')
            canvas.create_line(290, 10, 210, 90, width=5, fill="black", tag='equis')
            Game[0][2]=1
            turn = 0
        else:
            canvas.create_oval(210, 10, 290, 90, width=5, fill='white', tag='circulo') 
            Game[0][2]=-1
            turn = 1
     # Second block
    if event.x < 100 and event.y > 100 and event.y <200 and Game[1][0]==0:
        if turn == 1:
            canvas.create_line(10, 110, 90, 190, width=5, fill="black", tag='equis')
            canvas.create_line(90, 110, 10, 190, width=5, fill="black", tag='equis')
            Game[1][0]=1
            turn = 0
        else:
            canvas.create_oval(10, 110, 90, 190, width=5, fill='white', tag='circulo') 
            Game[1][0]=-1
            turn = 1
    if event.x > 100 and event.x <200 and event.y > 100 and event.y <200 and Game[1][1]==0:
        if turn == 1:
            canvas.create_line(110, 110, 190, 190, width=5, fill="black", tag='equis')
            canvas.create_line(190, 110, 110, 190, width=5, fill="black", tag='equis')
            Game[1][1]=1
            turn = 0
        else:
            canvas.create_oval(110, 110, 190, 190, width=5, fill='white', tag='circulo') 
            Game[1][1]=-1
            turn = 1
    if event.x > 200 and event.y > 100 and event.y <200 and Game[1][2]==0:
        if turn == 1:
            canvas.create_line(210, 110, 290, 190, width=5, fill="black", tag='equis')
            canvas.create_line(290, 110, 210, 190, width=5, fill="black", tag='equis')
            Game[1][2]=1
            turn = 0
        else:
            canvas.create_oval(210, 110, 290, 190, width=5, fill='white', tag='circulo') 
            Game[1][2]=-1
            turn = 1
    # Third block
    if event.x < 100 and event.y > 200 and Game[2][0]==0:
        if turn == 1:
            canvas.create_line(10, 210, 90, 290, width=5, fill="black", tag='equis')
            canvas.create_line(90, 210, 10, 290, width=5, fill="black", tag='equis')
            Game[2][0]=1
            turn = 0
        else:
            canvas.create_oval(10, 210, 90, 290, width=5, fill='white', tag='circulo') 
            Game[2][0]=-1
            turn = 1
    if event.x > 100 and event.x < 200 and event.y > 200 and Game[2][1]==0:
        if turn == 1:
            canvas.create_line(110, 210, 190, 290, width=5, fill="black", tag='equis')
            canvas.create_line(190, 210, 110, 290, width=5, fill="black", tag='equis')
            Game[2][1]=1
            turn = 0
        else:
            canvas.create_oval(110, 210, 190, 290, width=5, fill='white', tag='circulo') 
            Game[2][1]=-1
            turn = 1
    if event.x > 200 and event.y > 200 and Game[2][2]==0:
        if turn == 1:
            canvas.create_line(210, 210, 290, 290, width=5, fill="black", tag='equis')
            canvas.create_line(290, 210, 210, 290, width=5, fill="black", tag='equis')
            Game[2][2]=1
            turn = 0
        else:
            canvas.create_oval(210, 210, 290, 290, width=5, fill='white', tag='circulo') 
            Game[2][2]=-1
            turn = 1
    # For look the action game        
    print(f'click on: x:{event.x}, y:{event.y} {Game}') 

canvas.bind("<Button-1>", ClickCanvas)
# Some important functions for game functionality
def ReStart():
    canvas.delete('equis')
    canvas.delete('circulo')
    canvas.delete('Win')
    space = True
    for x in range(3):
        for y in range(3):
            Game[x][y]=0
def Draw():
    global space
    space = False
    for x in range(3):
        for y in range(3):
            if Game[x][y]== 0:
                space = True
    return space

def winXY(A,B,C):
    if (A == 1 and B == 1 and C ==1):
        return [True, 'X']
    elif (A == -1 and B == -1 and C ==-1):
        return [True, 'O']
    else:
         return [False, 0]

winProcess = None
def IsWin():
    global winProcess, Game, winsX, winsO, turn
    W = [False,0]

    # Ways to win horizontally
    A = winXY(Game[0][0], Game[0][1] ,Game[0][2])
    if A[0]:
        canvas.create_line(10, 50, 290, 50, width = 5, fill='red', tag= 'Win')
        W = A
    B = winXY(Game[1][0], Game[1][1] ,Game[1][2])
    if B[0]:
        canvas.create_line(10, 150, 290, 150, width = 5, fill='red', tag= 'Win')
        W = B
    C = winXY(Game[2][0], Game[2][1] ,Game[2][2])
    if C[0]:
        canvas.create_line(10, 250, 290, 250, width = 5, fill='red', tag= 'Win')
        W=C
    # Ways to win vertically
    D = winXY(Game[0][0], Game[1][0] ,Game[2][0])
    if D[0]:
        canvas.create_line(50, 10, 50, 290, width = 5, fill='red', tag= 'Win')
        W = D
    E = winXY(Game[0][1], Game[1][1] ,Game[2][1])
    if E[0]:
        canvas.create_line(150, 10, 150, 290, width = 5, fill='red', tag= 'Win')
        W = E
    F = winXY(Game[0][2], Game[1][2] ,Game[2][2])
    if F[0]:
        canvas.create_line(250, 10, 250, 290, width = 5, fill='red', tag= 'Win')
        W = F
    # Ways to win with cross style
    H = winXY(Game[0][0], Game[1][1] ,Game[2][2])
    if H[0]:
        canvas.create_line(10, 10, 290, 290, width = 5, fill='red', tag= 'Win')
        W=H
    G = winXY(Game[0][2], Game[1][1] ,Game[2][0])
    if G[0]:
        canvas.create_line(10, 290, 290, 10, width = 5, fill='red', tag= 'Win')
        W=G
    # Revew of the winner
    if W[0]:
        if W[1]=='X':
            winsX+=1
            X['text'] = f'X = {winsX}'
        else:
            winsO+=1
            O['text'] = f'O= {winsO}'
        messagebox.showinfo('Ganador!', f'Jugador {W[1]} ha ganado!')
        turn = 0
        ReStart()
        winProcess = canvas.after(1000, IsWin)
    else:
        if not Draw():
            messagebox.showinfo('Alerta', 'Se han acabado los espacios, esto es un empate:c')
            ReStart()
        winProcess = canvas.after(1000, IsWin)
IsWin()
# Main loop
MainWindow.mainloop()