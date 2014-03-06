Arpy
====

Arpy is an algorithmic music generator written in python that was created for a course at Cal Poly San Luis Obispo.

Arpy is called like this:

'''
from src.arp import Arpy
from src.arp.Arpy import Arpy
from src.arp.ArpNote import ArpNote
from src.arp.ArpNote import Note
from src.arp.Arpy import Progression

# from src.gui import ArpGui

key = ArpNote()
key.pitch = Note.C
key.volume = 100
arp = Arpy(key, Progression.minor)
bars = arp.genBars(32)
Arpy.makeMidiFromNotes(bars)
'''