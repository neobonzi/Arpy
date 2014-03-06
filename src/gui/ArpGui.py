#-----------------------------------------------------------------------------
# Name:        Arpy.py
# Purpose:     Generate an arpegiatted midi file
#
# Author:      James Bilous
#
# Created:     2014/02/24
#-----------------------------------------------------------------------------

#!/usr/bin/python
from Tkinter import *

# Make the gui window
root = Tk()

# Initialize gui elements
# Header
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Arpy the Midi Arpeggiator!")
label.pack()

# Radios
key = IntVar()
R1 = Radiobutton(root, text="C", variable=key, value=1)
R1.pack( side = LEFT )

R2 = Radiobutton(root, text="Db", variable=key, value=2)
R2.pack( side = LEFT )

R3 = Radiobutton(root, text="D", variable=key, value=3)
R3.pack( side = LEFT )

R4 = Radiobutton(root, text="Eb", variable=key, value=4)
R4.pack( side = LEFT )

R5 = Radiobutton(root, text="E", variable=key, value=5)
R5.pack( side = LEFT )

R6 = Radiobutton(root, text="F", variable=key, value=6)
R6.pack( side = LEFT )

R7 = Radiobutton(root, text="Gb", variable=key, value=7)
R7.pack( side = LEFT )

R8 = Radiobutton(root, text="G", variable=key, value=8)
R8.pack( side = LEFT )

R9 = Radiobutton(root, text="Ab", variable=key, value=9)
R9.pack( side = LEFT )

R10 = Radiobutton(root, text="A", variable=key, value=10)
R10.pack( side = LEFT )

R11 = Radiobutton(root, text="Bb", variable=key, value=11)
R11.pack( side = LEFT )

R12 = Radiobutton(root, text="B", variable=key, value=12)
R12.pack( side = LEFT )

SubmitBtn = Button( root, text="Generate" )

SubmitBtn.pack()

root.mainloop()