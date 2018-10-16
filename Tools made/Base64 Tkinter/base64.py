#!/usr/bin/python2.7
from Tkinter import *
import base64

# ********* Functions related to base64 ***************

def base64encode(event) :
	l = len(str(entry2.get()))
	entry2.delete(0,l)
	e1 = str(entry1.get())
	e2 = base64.b64encode(e1)
	entry2.insert(0,e2)

def base64decode(event) :
	l = len(str(entry4.get()))
	entry4.delete(0,l)
	e3 = str(entry3.get())
	e4 = base64.b64decode(e3)
	entry4.insert(0,e4)

def cleartextencode(event) :
	l1 = len(str(entry1.get()))
	l2 = len(str(entry2.get()))
	entry1.delete(0,l1)
	entry2.delete(0,l2)

def cleartextdecode(event) :
	l1 = len(str(entry3.get()))
	l2 = len(str(entry4.get()))
	entry3.delete(0,l1)
	entry4.delete(0,l2)

# ******** Base64 functions ends **********************

screen = Tk()

screen.title("Tools")

# ******************* All about Base64 *****************

# *****************Base 64 encode *********************

heading = Label(screen, text="All about Base64")
heading.config(font=("Courier",32))
heading.grid(row=0,columnspan=2,pady=10)

Label(screen, text="Input String: ").grid(row=1, sticky=E, padx=4, pady=10)
entry1 = Entry(screen, width=50)
entry1.grid(row=1, column=1, padx=4, sticky=W, pady=10)

Label(screen, text="Base64 Encoded: ").grid(row=2, sticky=E, padx=4, pady=10)
entry2 = Entry(screen, width=50)
entry2.grid(row=2,column=1,padx=4,sticky=W, pady=10)

encodebutton = Button(screen,text="ENCODE")
encodebutton.bind("<Button-1>", base64encode)
encodebutton.grid(row=3,column=1,sticky=W, pady=10)
clearbuttonencode = Button(screen,text="Clear")
clearbuttonencode.bind("<Button-1>",cleartextencode)
clearbuttonencode.grid(row=3,column=1)

# *******************Base64 encode ends ********************

# ********************Base64 decode ************************

Label(screen, text="Input String: ").grid(row=4, sticky=E, padx=4, pady=10)
entry3 = Entry(screen, width=50)
entry3.grid(row=4, column=1, padx=4, sticky=W, pady=10)

Label(screen, text="Base64 Decoded: ").grid(row=5, sticky=E, padx=4, pady=10)
entry4 = Entry(screen, width=50)
entry4.grid(row=5,column=1,padx=4,sticky=W, pady=10)

decodebutton = Button(screen,text="DECODE")
decodebutton.bind("<Button-1>", base64decode)
decodebutton.grid(row=6,column=1,sticky=W, pady=10)
clearbuttondecode = Button(screen,text="Clear")
clearbuttondecode.bind("<Button-1>",cleartextdecode)
clearbuttondecode.grid(row=6,column=1)

# ***********************Base64 decode ends ****************

screen.mainloop()