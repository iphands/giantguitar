import json
import threading
import time
from Queue import Queue

class Player(object):
    def __init__(self, sounder):
        self.sounder = sounder
        with open('chords.js') as file:
            self.chords = json.load(file)
        #print(self.chords)

    def chord(self, k):
        print (self.chords[k])
        for s_str in self.chords[k]:
            s = int(s_str)
            self.sounder.fret(s, self.chords[k][s_str])

    def check_song(self, name, song):
        for e in song["chords"]:
            if not e[0] in self.chords:
                raise Exception("Song {} asks for chord {} but that chord is not defined in chords.js".format(name, e[0]))

    def song(self, name):
        with open("songs/" + name + ".js") as file:
            song = json.load(file)
            self.check_song(name, song)
            q = { "play": Queue(), "control": Queue() }
            threading.Thread(target=worker, args=(q, name, song)).start()
            return q

def worker(q, name, song):
    tempo = int(song["tempo"])
    whole = (60000 / tempo) * 4
    print("\n\nPlaying: {} at tempo {} (a whole note is {}ms)\n\n".format(name, tempo, whole))
    for e in song["chords"]:
        if not q["control"].empty():
            if q["control"].get_nowait() == "stop":
                break
        q["play"].put(e[0])
        time.sleep((whole / 1000.0) * e[1])
        
        
