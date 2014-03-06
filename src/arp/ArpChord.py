#-----------------------------------------------------------------------------
# Name:        Arpy.py
# Purpose:     Generate an arpegiatted midi file
#
# Author:      James Bilous
#
# Created:     2014/02/24
#-----------------------------------------------------------------------------

import struct,  sys,  math
from src.midiutil.MidiFile import MIDIFile
import ArpNote

class ArpChord():
   notes = []

   '''
   Represents a note in an arpeggio
   '''
   def __init__(self):
      self.type = 'Unknown'
      notes = []

   def __init__(self, notes):
      self.notes = notes

   def __eq__(self, other):
      return self.note == other.note


