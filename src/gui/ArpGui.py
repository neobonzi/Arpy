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
from src.arp import Arpy
from src.arp.Arpy import Arpy
from src.arp.ArpNote import ArpNote
from src.arp.ArpNote import Note
from src.arp.Arpy import Progression
import thread
import Queue

class ArpyLiveApp:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack

# Make the gui window
root = Tk()

# Initialize gui elements
# Header
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Arpy the Midi Arpeggiator!")
label.pack()

StartBtn = Button( root, text="Start", command=startArp)

StartBtn.pack()

key = ArpNote()
key.pitch = Note.C
key.volume = 100
arp = Arpy(key, Progression.minor)
bars = arp.genBars(4)

# Radios
# key = IntVar()
# R1 = Radiobutton(root, text="C", variable=key, value=1)
# R1.pack( side = LEFT )

# R2 = Radiobutton(root, text="Db", variable=key, value=2)
# R2.pack( side = LEFT )
# A
# R3 = Radiobutton(root, text="D", variable=key, value=3)
# R3.pack( side = LEFT )

# R4 = Radiobutton(root, text="Eb", variable=key, value=4)
# R4.pack( side = LEFT )

# R5 = Radiobutton(root, text="E", variable=key, value=5)
# R5.pack( side = LEFT )

# R6 = Radiobutton(root, text="F", variable=key, value=6)
# R6.pack( side = LEFT )

# R7 = Radiobutton(root, text="Gb", variable=key, value=7)
# R7.pack( side = LEFT )

# R8 = Radiobutton(root, text="G", variable=key, value=8)
# R8.pack( side = LEFT )

# R9 = Radiobutton(root, text="Ab", variable=key, value=9)
# R9.pack( side = LEFT )

# R10 = Radiobutton(root, text="A", variable=key, value=10)
# R10.pack( side = LEFT )

# R11 = Radiobutton(root, text="Bb", variable=key, value=11)
# R11.pack( side = LEFT )

# R12 = Radiobutton(root, text="B", variable=key, value=12)
# R12.pack( side = LEFT )


root.mainloop()