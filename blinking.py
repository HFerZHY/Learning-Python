import tkinter as tk
import time
import tkinter.font as tkFont
import random as rd

window = tk.Tk()
window.title('变色')
var = 'Hello World'
ft1 = tkFont.Font(family='Arial', size=30, weight=tkFont.BOLD)

def SXH():
	while True:
		i = hex(rd.randint(0, 16777216))     #Initialize Random Color
		l = str(i)[2:]                       #Change to String
		if len(l) != 6:
			l = l.rjust(6, '0')              #Filter and Correct 0 Starting Ones
		l = '#' + l                          #Formatting
		w.create_text(200, 50, text = var, fill = l , font = ft1, tag = 'S')
		window.update()
		time.sleep(0.5)
		w.delete('S')

def ENT():
	global var
	var = e.get()

w = tk.Canvas(window, bg = '#FFFFFF', width = 400, height = 100)
w.pack()

e = tk.Entry(window, width = 50)
e.pack()

b = tk.Button(window, text = 'Change Text', command = ENT)
b.pack()

SXH()

window.mainloop()