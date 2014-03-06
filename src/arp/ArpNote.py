#-----------------------------------------------------------------------------
# Name:        Arpy.py
# Purpose:     Generate an arpegiatted midi file
#
# Author:      James Bilous
#
# Created:     2014/02/24
#-----------------------------------------------------------------------------

import struct,  sys,  math, random

class Note:
   A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab = range(69, 81)

class ArpNote():

   # Start times and end times are relative to the chord.
   pitch = 0
   volume = 0
   time = 0
   duration = 0.0

   '''
   Represents a note in an arpeggio
   '''
   def __init__(self):
      self.type = 'ArpNote'

   '''
   There are 12 notes in an octave, so module 12 notes are equivalent
   '''
   def __eq__(self, other):
      return cmp(self.pitch % 12, other.pitch % 12)
