import json
import threading
import time

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
            song = json.load(file)
            threading.Thread(target=worker, args=(self, self.sounder, name, song)).start()

def worker(player, sounder, name, song):
    print("Playing: {} at tempo {}".format(name, song["tempo"]))
    tempo = int(song["tempo"])
    for e in song["chords"]:
        print(e)
        player.chord(e[0])
        time.sleep(1)
        
        
