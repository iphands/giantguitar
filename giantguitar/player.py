import json
import threading
import time
from Queue import Queue

class Player(object):
    def __init__(self, sounder):
        self.sounder = sounder
        with open('chords.js') as file:
            self.chords = json.load(file)
        print(self.chords)

    def chord(self, k):
        print (self.chords[k])
        for s_str in self.chords[k]:
            s = int(s_str)
            self.sounder.fret(s, self.chords[k][s_str])

    def song(self, name):
        with open("songs/" + name + ".js") as file:
            q = Queue()
            song = json.load(file)
            threading.Thread(target=worker, args=(q, name, song)).start()
            return q

def worker(q, name, song):
    print("Playing: {} at tempo {}".format(name, song["tempo"]))
    tempo = int(song["tempo"])
    for e in song["chords"]:
        print(e)
        q.put(e[0])
        time.sleep((tempo / 1000.0) * e[1])
        
        
