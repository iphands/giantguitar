import json
import threading
import time
import subprocess
from Queue import Queue


class Player(object):
    def __init__(self, sounder):
        self.sounder = sounder
        with open('chords.js') as file:
            self.chords = json.load(file)

    def chord(self, k):
        c = self.chords[k]
        # print ("chord is: " + c)
        if k == "r":
            print("resting")
            self.sounder.mute()
        else:
            for s_str in c:
                s = int(s_str)
                self.sounder.fret(s, c[s_str])

    def check_song(self, name, song):
        for e in song["chords"]:
            if not e[0] in self.chords:
                raise Exception("Song {} asks for chord {} but that chord is not defined in chords.js".format(name, e[0]))

    def song(self, name):
        with open("songs/" + name + ".js") as file:
            song = json.load(file)
            self.check_song(name, song)
            subprocess.call('echo "Welcome to geekSPARK... the Giant Guitar is going to play ' + song["name"]  + '" | festival --tts', shell=True)
            q = { "play": Queue(), "control": Queue(), "sig": "playing" }
            threading.Thread(target=worker, args=(q, name, song)).start()
            return q

def worker(q, name, song):
    tempo = int(song["tempo"])
    tempo = tempo * 1.2
    whole = (60000 / tempo) * 4
    print("\n\nPlaying: {} at tempo {} (a whole note is {}ms)\n\n".format(name, tempo, whole))

    for chord in song["chords"]:
        q["sig"] = "playing"
        if not q["control"].empty():
            if q["control"].get_nowait() == "stop":
                break
        q["play"].put(chord[0])
        time.sleep((whole / 1000.0) * chord[1])
    q["sig"] = "stopped"
