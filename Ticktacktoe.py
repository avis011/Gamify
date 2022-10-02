from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("TIC TAC TOE - Hardik")

x = 0

ff = Frame(root, relief=SUNKEN, borderwidth=4)
t = Label(ff, text="Player 1:'X'  |    Player2:'O'").pack()
ff.grid(row=0, column=0)

player_pos = {'X':[], 'O':[]}


def check_win(player_pos, cur_player):

    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):


            return True

    return False




def isfull():
    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for i in buttons:
        if i.cget('text') == '':
            return False
    return True


def check():
      global player_pos,x
      # print(player_pos)
      if check_win(player_pos,'X'):
          x = 0
          player_pos = {'X': [], 'O': []}
          messagebox.showinfo('Winner!!!!',"Player 1 with \'X\' option Won the game ")
          res = messagebox.askquestion("Game Over", 'Player 1 with \'X\' option Won the game. \n Want to play new game')
          if res == 'no':
              root.destroy()
          else:
              for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
                  i.config(text='')

      elif check_win(player_pos,'O'):
          x = 0
          player_pos = {'X':[], 'O':[]}
          messagebox.showinfo('Winner!!!!',"Player 2 with \'O\' option Won the game ")
          res = messagebox.askquestion("Game Over", 'Player 2 with \'O\' option Won the game. \n Want to play new game')
          if res == 'no':
              root.destroy()
          else:
              for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
                  i.config(text='')

      if isfull():
        res = messagebox.askquestion("Game Tie", 'Board is full. \n Want to play new game')
        if res == 'no':
            root.destroy()
        else:
            for i in [b1, b2, b3, b4, b5, b6, b7, b8, b9]:
                i.config(text='')


def click(num):
    global x
    if num == 1:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"

        x += 1

        if b1.cget('text') == '':
            b1.config(text=sign)
            if b1.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)

    if num == 2:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b2.cget('text') == '':
            b2.config(text=sign)
            if b2.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    if num == 3:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b3.cget('text') == '':
            b3.config(text=sign)
            if b3.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    if num == 4:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b4.cget('text') == '':
            b4.config(text=sign)
            if b4.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)

    if num == 5:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b5.cget('text') == '':
            b5.config(text=sign)
            if b5.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    if num == 6:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b6.cget('text') == '':
            b6.config(text=sign)
            if b6.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    if num == 7:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b7.cget('text') == '':
            b7.config(text=sign)
            if b7.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)

    if num == 8:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b8.cget('text') == '':
            b8.config(text=sign)
            if b8.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    if num == 9:
        if x % 2 == 0:
            sign = "X"
        elif x % 2 != 0:
            sign = "O"
        x += 1
        if b9.cget('text') == '':
            b9.config(text=sign)
            if b9.cget('text') == 'X':
                player_pos['X'].append(num)
            else:
                player_pos['O'].append(num)
    check()


f1 = Frame(root, height=10, width=10,relief=RAISED,borderwidth=4)
f2 = Frame(root, height=10, width=10,relief=RAISED,borderwidth=4)
f3 = Frame(root, height=10, width=10,relief=RAISED,borderwidth=4)
b1 = Button(f1, height=10, width=15, command=lambda: click(1))
b2 = Button(f1, height=10, width=15, command=lambda: click(2))
b3 = Button(f1, height=10, width=15, command=lambda: click(3))
b4 = Button(f2, height=10, width=15, command=lambda: click(4))
b5 = Button(f2, height=10, width=15, command=lambda: click(5))
b6 = Button(f2, height=10, width=15, command=lambda: click(6))
b7 = Button(f3, height=10, width=15, command=lambda: click(7))
b8 = Button(f3, height=10, width=15, command=lambda: click(8))
b9 = Button(f3, height=10, width=15, command=lambda: click(9))
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
f1.grid(row=1, column=0)
f2.grid(row=1, column=1)
f3.grid(row=1, column=2)

root.mainloop()
