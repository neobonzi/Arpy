from Tkinter import *
from ..arp import Arpy
from ..arp.Arpy import Arpy
from ..arp.ArpNote import ArpNote
from ..arp.ArpNote import Note
from ..arp.Arpy import Progression

import threading 
import Queue
import os


class ArpyGUI:


    def __init__(self, master):
        self.master = master
        # Radios
        self.numBars = StringVar()
        self.delayTime = StringVar()
        self.mode = IntVar()

        # Labels
        Label(master, text="Bars:").grid(row=0, column=0)
        Label(master, text="Speed:").grid(row=0, column=2)
        Label(master, text="Key:").grid(row=1, column=0)
        Label(master, text="Mode:").grid(row=2, column=0)

        self.barsEntry = Entry( self.master, textvariable=self.numBars )
        self.barsEntry.grid(row=0,column=1)

        self.speedEntry = Entry( self.master, textvariable=self.delayTime )
        self.speedEntry.grid(row=0,column=3)

        self.initKeyRadios()
        self.initModeRadios()

        self.startBtn = Button( self.master, text="Start", command=self.startArp)
        self.stopBtn = Button( self.master, text="Stop", command=self.stopArp)

        self.queue = Queue.Queue()
        
        self.startBtn.grid(row=0, column=8)
        self.stopBtn.grid(row=1, column=8)

    def initModeRadios(self):
        R1 = Radiobutton(root, text="Ionian", variable=self.mode, value=1)
        R1.grid(row=3, column=1)

        R2 = Radiobutton(root, text="Dorian", variable=self.mode, value=2)
        R2.grid(row=3, column=2)

        R3 = Radiobutton(root, text="Phrygian", variable=self.mode, value=3)
        R3.grid(row=3, column=3)

        R4 = Radiobutton(root, text="Lydian", variable=self.mode, value=4)
        R4.grid(row=3, column=4)

        R5 = Radiobutton(root, text="Mixolydian", variable=self.mode, value=5)
        R5.grid(row=3, column=5)

        R6 = Radiobutton(root, text="Aeolian", variable=self.mode, value=6)
        R6.grid(row=3, column=6)

        R7 = Radiobutton(root, text="Locrian", variable=self.mode, value=7)
        R7.grid(row=3, column=7)


    def initKeyRadios(self):
        self.key = IntVar()
        R1 = Radiobutton(root, text="C", variable=self.key, value=69)
        R1.grid(row=1, column=1)

        R2 = Radiobutton(root, text="Db", variable=self.key, value=70)
        R2.grid(row=1, column=2)

        R3 = Radiobutton(root, text="D", variable=self.key, value=71)
        R3.grid(row=1, column=3)

        R4 = Radiobutton(root, text="Eb", variable=self.key, value=72)
        R4.grid(row=1, column=4)

        R5 = Radiobutton(root, text="E", variable=self.key, value=73)
        R5.grid(row=1, column=5)

        R6 = Radiobutton(root, text="F", variable=self.key, value=74)
        R6.grid(row=1, column=6)

        R7 = Radiobutton(root, text="Gb", variable=self.key, value=75)
        R7.grid(row=2, column=1)

        R8 = Radiobutton(root, text="G", variable=self.key, value=76)
        R8.grid(row=2, column=2)

        R9 = Radiobutton(root, text="Ab", variable=self.key, value=77)
        R9.grid(row=2, column=3)

        R10 = Radiobutton(root, text="A", variable=self.key, value=78)
        R10.grid(row=2, column=4)

        R11 = Radiobutton(root, text="Bb", variable=self.key, value=79)
        R11.grid(row=2, column=5)

        R12 = Radiobutton(root, text="B", variable=self.key, value=80)
        R12.grid(row=2, column=6)


    def startArp(self):
        key = ArpNote()
        key.pitch = self.key.get()
        key.volume = 100
        progression = Progression.Ionian

        if self.mode.get() == 1:
            progression = Progression.Ionian
        elif self.mode.get() == 2:
            progression = Progression.Dorian
        elif self.mode.get() == 3:
            progression = Progression.Phrygian
        elif self.mode.get() == 4:
            progression = Progression.Lydian
        elif self.mode.get() == 5:
            progression = Progression.Mixolydian
        elif self.mode.get() == 6:
            progression = Progression.Aeolian
        else:
            progression = Progression.Lydian

        arp = Arpy(key, progression)
        arp.speed = float(str(self.speedEntry.get()))
        arp.genBars(int(str(self.barsEntry.get())))

    def stopArp(self):
        print "stop"



# uber-main
root = Tk()
ui = ArpyGUI(root)

root.mainloop()