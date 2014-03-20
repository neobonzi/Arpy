#---------------------------- -------------------------------------------------
# Name:        Arpy.py
# Purpose:     Generate an arpegiatted midi file
#
# Author:      James Bilous
#
# Created:     2014/02/24
#-----------------------------------------------------------------------------

import struct,  sys,  math, random, logging, copy, time, rtmidi
import ArpChord
from ArpNote import ArpNote
from src.midiutil.MidiFile import MIDIFile


class Step():
   half, whole = range(1,3)

class Progression():
   Ionian = [Step.whole, Step.whole, Step.half, Step.whole, Step.whole, Step.whole, Step.half]
   Dorian = [Step.whole, Step.half, Step.whole, Step.whole, Step.whole, Step.half, Step.whole]
   Phrygian = [Step.half, Step.whole, Step.whole, Step.whole, Step.half, Step.whole, Step.whole]
   Lydian = [Step.whole, Step.whole, Step.whole, Step.half, Step.whole, Step.whole, Step.half]
   Mixolydian = [Step.whole, Step.whole, Step.half, Step.whole, Step.whole, Step.half, Step.whole]
   Aeolian = [Step.whole, Step.half, Step.whole, Step.whole, Step.half, Step.whole, Step.whole]
   Locrian = [Step.half, Step.whole, Step.whole, Step.half, Step.whole, Step.whole, Step.whole]
class Chords():
   triad = [2, 2, 3]

class Arpy():

   '''
   The class that generates arpegiatted midi files
   '''
   def __init__(self, key, progression):
      self.type = 'Arpy'
      self.progression = progression
      self.out  = rtmidi.MidiOut()
      self.speed = .156
      if self.out.get_ports():
          self.out.open_port(0)
      else:
          self.out.open_virtual_port("My virtual output")
      self.key = key
      self.activeNotes = []
      self.time = 0

   '''
   Sends a chunk of midi notes live, baby, live!
   Todo: Queue and parallelism
   '''
   def sendNotes(self, notes):
      self.liveTime = 0

      while notes or self.activeNotes:
         print "here are the notes"
         print notes
         print " there go the notes"
         print self.activeNotes
         for activeNote in self.activeNotes:
            if activeNote.duration == 0:
               message = [0x80 + activeNote.track, activeNote.pitch, 0]
               self.out.send_message(message)
               self.activeNotes.pop(self.activeNotes.index(activeNote))
            else:
               activeNote.duration -= 1

         while notes and (self.liveTime == notes[0].time):
            newNote = notes.pop(0)
            self.activeNotes.extend([newNote])
            message = [0x90 + newNote.track, newNote.pitch, 50]
            self.out.send_message(message)
         
         self.liveTime += 1
         time.sleep(self.speed)
         print "loop done"

   def genNextRoot(self):

      start = self.key
      for curNote in range(0, random.randint(0,7)):
         start += self.progression[curNote]
      return start

   '''
   Generates numBars bars in the key of self.key
   '''
   def genBars(self, numBars):
      notes = []
      bpMeasure = 4

      for num in range(0,numBars):
         notes.extend(self.genBar(bpMeasure))

      self.sendNotes(notes)

   '''
   Generate a scale in the mode of the given Arpy object in the key of rootNote
   '''
   def genScale(self, rootNote):
      mode = self.progression
      scale = []

      for index in range(0, 7):
         newNote = ArpNote()
         newNote.pitch = rootNote.pitch + sum(mode[0:index])
         scale.extend([newNote])

      return scale


   '''
   Adapt a scale to be in the key of the given Arpy object
   '''
   def adaptScale(self, scale):
      #First generate the scale in the Arpy objects key
      rootScale = self.genScale(self.key)

      #Now take each notes pitch value and take the 12th modulo
      for scaleIndex in range(len(scale)):
         found = False
         for rootScaleIndex in range(len(rootScale)):
            if (cmp(scale[scaleIndex], rootScale[rootScaleIndex])):
               found = True

         #If the note in the scale is not in our key, flat it 
         if not found:
            scale[scaleIndex].pitch -= 1

   '''
   Generate a single measure given an arpy object and a number of beats
   '''
   def genBar(self, bpMeasure):
      volume = 100
      notes = []
      progIndex = 0
      time = self.time

      # Beats per note, default 1
      noteDuration = 1

      # Get a random note in the scale
      myPitch = self.key.pitch
      newRoot = ArpNote()
      newRoot.pitch = myPitch + sum(self.progression[0:random.randint(1,6)])

      # Get a scale starting from the new root in the given mode
      newScale = self.genScale(newRoot)

      # Now adapt the scale so its in the current key
      self.adaptScale(newScale)

      intervalIndex = 0
      chordIndex = 0
      octave = 0
      inverse = False
      chordType = Chords.triad

      # New Feature! Sicky Tight. Add the main triad as a chord
      triad1 = copy.copy(newScale[0])
      triad2 = copy.copy(newScale[2])
      triad3 = copy.copy(newScale[4])

      triad1.pitch -= 24
      triad1.time = time
      triad1.track = 2
      triad1.volume = volume
      triad2.pitch -= 24
      triad2.track = 2
      triad2.time = time
      triad2.volume = volume
      triad3.pitch -= 24
      triad3.track = 2
      triad3.time = time
      triad3.volume = volume

      notes.extend([triad1,triad2,triad3])

      startTime = self.time

      # Arpeggiate up the scale bpMeasure number of times
      for note in range(0, bpMeasure):

         noteDuration = random.sample([1, 2, 4], 1)[0]

         newNote = copy.copy(newScale[chordIndex])
         newNote.time = time
         newNote.duration = noteDuration
         newNote.volume = volume
         newNote.track = 1
         newNote.pitch += octave * 12  
         notes.extend([newNote])

         # Determine whether we should go up or down
         # Time to toot my own horn. This is really cool and looks slick because of
         # python slicing. The chord progression you choose will be rotated like a dial
         # so a random of -1 will turn [ 2, 2, 3] for example, into [ 3, 3, 2]
         # Take the 0th element and bam, you have how far to go for the next note

         updown = random.sample([-1, 1], 1)[0]

         if updown > 0 :
            chordType = chordType[1:] + chordType[:1]
            chordIndex -= chordType[0]
         else:
            chordType = chordType[-1:] + chordType[:-1]
            chordIndex += chordType[0]

         # Handle wraparound
         if chordIndex > 6:
            chordIndex -= 7
            octave += 1
         elif chordIndex < 0:
            octave -= 1
            chordIndex += 7

         # Move up the current time 
         time += newNote.duration
         self.time = time
      
      triad1.duration = triad2.duration = triad3.duration = (time - startTime)

      return notes



   '''
   Returns an ArpNote that is scaleIndex notes up the scale from self.key
   '''
   def makeNoteFromScaleIndex(self, scaleIndex):

      newNote = ArpNote()
      newNote.pitch = self.key.pitch

      for intervalIndex in range(0, scaleIndex):
         newNote.pitch += self.progression[intervalIndex]

      return newNote

   def makeScaleIndexFromNote(self, note):

      testNote = self.root
      scaleIndex = 0

      while cmp(testNote, note) != 0:
         testNote.pitch += 1
         scaleIndex += 1

      return scaleIndex

   @staticmethod
   def makeMidiFromNotes(notes):
      midiOut = MIDIFile(1)
      for curNote in range(0, len(notes)):
         note = notes[curNote]
         midiOut.addNote(0, 0, note.pitch, note.time, note.duration, note.volume)
      
      binfile = open("output.mid", 'wb')
      midiOut.writeFile(binfile)
      binfile.close()
