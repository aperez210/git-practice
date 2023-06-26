from midiutil import MIDIFile
import midiutil as mu
import os
    
FILE_NAME = "MIDIFILE.midi"
try:
    f = open(FILE_NAME, "xb")
except:
    os.remove(FILE_NAME)
    f = open(FILE_NAME, "xb")
NUM_TRACKS = 3

class superMidi(MIDIFile):
    def closeFile(self):
        self.writeFile(f)
        f.close()
            
    def addMajScale(self,p:int,d:float):
        for head in range(8):
            self.addNote(0,0,p,head*d,d,100)
            if(head == 2) or (head == 6):
                p+=1
            else:
                p+=2

    def addMinScale(self,p:int,d:float,loc:float):
        for head in range(16):
            self.addNote(0,0,p,head*d + loc,d,100)
            if(head < 7):
                if(head == 1) or (head == 4):
                    p+=1
                else:
                    p+=2
            else:
                if (head == 11) or (head == 14):
                    p-=1
                else:
                    p-=2
            

    def addHarMin(self,p:int,d:float,loc:float):
        for head in range(16):
            self.addNote(0,0,p,head*d + loc,d,100)
            if(head < 7):
                if(head == 5):
                    p+=3
                elif(head == 1) or (head == 4) or (head == 6):
                    p+=1
                else:
                    p+=2
            else:
                if(head == 8):
                    p-=3
                elif(head == 7) or (head == 9) or (head == 12):
                    p-=1
                else:
                    p-=2
    def ink(self,l:list,m:int) -> list:
        out = [-1,0]
        head = 0
        length = 0
        for sect in l:
            len = sect*m
            head += len
            out.append(head)
            length+=1
        out[0] = length
        print(out)
        return out

    def addLoop(self,p:int):
        meter = 4
        Section = self.ink([16,1,1,1,1],meter)
        for x in range(Section[Section[0]]):
            try:
                sectXStart = Section[x+1]
                sectXEnd = Section[x+2]
            except:
                sectXStart = -1
                sectXEnd = -1
            if x == 0:
                for x in range(sectXStart,sectXEnd):
                    measureLoc = x%(meter*2)
                    if  measureLoc == 0:
                        self.addNote(1,0,p,x,.25,100)
                        self.addNote(1,0,p,x+.5,.25,100)
                        self.addNote(1,0,p,x+.75,.25,100)
                        self.addNote(1,0,p+5,x,.25,100)
                        self.addNote(1,0,p+5,x+.5,.25,100)
                        self.addNote(1,0,p+5,x+.75,.25,100)
                    if measureLoc == 1:
                        self.addNote(1,0,p,x+.5,.25,100)
                        self.addNote(1,0,p+5,x+.5,.25,100)
                    if measureLoc == 2:
                        self.addNote(1,0,p,x,.25,100)
                        self.addNote(1,0,p,x+.25,.25,100)
                        self.addNote(1,0,p+5,x,.25,100)
                        self.addNote(1,0,p+5,x+.25,.25,100)
                    if measureLoc == 3:
                        self.addNote(1,0,p,x,.25,100)
                        self.addNote(1,0,p,x+.5,.25,100)
                        self.addNote(1,0,p,x+.75,.25,100)
                        self.addNote(1,0,p+5,x,.25,100)
                        self.addNote(1,0,p+5,x+.5,.25,100)
                        self.addNote(1,0,p+5,x+.75,.25,100)
                    if measureLoc == 4:
                        self.addNote(1,0,p,x+.5,.25,100)
                        self.addNote(1,0,p+5,x+.5,.25,100)
                    if measureLoc == 5 or measureLoc == 6:
                        self.addNote(1,0,p,x,.25,100)
                        self.addNote(1,0,p,x+.25,.25,100)
                        self.addNote(1,0,p+5,x,.25,100)
                        self.addNote(1,0,p+5,x+.25,.25,100)
                    if measureLoc == 7:
                        self.addNote(1,0,p+1,x,.5,100)
                        self.addNote(1,0,p+6,x,.5,100)
            if x == 1:
                p+=5
            if x == 2:
                p+=4
            if x == 3:
                p-=3
            if x == 3:
                p-=3
            
            
        for head in range(Section[Section[0]+1]):
            if head == 8:
                self.addNote(0,0,p-7,head,2,100)
            if head == 10:
                self.addNote(0,0,p-7,head,2,100)
            if head == 12:
                self.addNote(0,0,p-7-12,head,2,100)
            if head == 14:
                self.addNote(0,0,p-7-12,head,2,100)
            if head == 4 * 4:
                self.addNote(0,0,p-7-12,head,1,100)
                self.addNote(0,0,p-7-12,head+1,1,100)
                self.addNote(0,0,p-7-12,head+2,1,100)
                self.addNote(0,0,p-7-12,head+3,1,100)
            if head == 5 * 4:
                self.addNote(0,0,p-7-12,head,1,100)
                self.addNote(0,0,p-7-12,head+1,1,100)
                self.addNote(0,0,p-7-12,head+2,1,100)
                self.addNote(0,0,p-7-11,head+3,1,100)
            if head == 6 * 4:
                self.addNote(0,0,p-7-12,head,1,100)
                self.addNote(0,0,p-7-12,head+1,1,100)
                self.addNote(0,0,p-7-12,head+2,1,100)
                self.addNote(0,0,p-7-12,head+3,1,100)
            if head == 7 * 4:
                self.addNote(0,0,p-7-12,head,1,100)
                self.addNote(0,0,p-7-12,head+1,1,100)
                self.addNote(0,0,p-7-12,head+2,1,100)
                self.addNote(0,0,p-7-11,head+3,1,100)


def midPattern(self):
    if x == 1:
        p+=0
    if x== 2:
        p+=9
    if x== 3:
        p-=3
    self.addHarMin(p,.5,sectXStart)
    for x in range(sectXStart,sectXEnd):
        measureLoc = x%meter
        if  measureLoc == 0:
            self.addNote(1,0,p,x,1,100)
        if measureLoc == 2:
            self.addNote(1,0,p-5,x,1,100)
        if measureLoc == 1 or measureLoc == 3:
            self.addNote(1,0,p+3,x,1,100)
            self.addNote(1,0,p+7,x,1,100)

def noteToOctaLib(p:int) -> list:
    lowNote = p%12
    currNote = lowNote
    out = []
    while currNote >= 255:
        out.append(currNote)
        currNote += 12
    return out
    

midiFile = superMidi(NUM_TRACKS,False,False,True,1,960,False)
#MIDIFile.addNote(track, channel, pitch, time, duration, volume, annotation=None)

midiFile.addLoop(48)
midiFile.addTempo(1,0,130)

midiFile.closeFile()        




