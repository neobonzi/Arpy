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