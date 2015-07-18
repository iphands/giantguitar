from pyo import *

class Player(object):


    def __init__(self):
        self.OPEN = {
            1: 329.63,
            2: 246.94,
            3: 196.00,
            4: 146.83,
            5: 110.00,
            6: 82.41
        }

        self.s = Server(audio="portaudio", nchnls=1, duplex=0).boot()
        self.strings = {}
        for i in range(1, 7):
            self.strings[i] = Sine(self.OPEN[i], 0, 0.1)

        self.fret(5, 2)
        self.fret(4, 2)
        self.fret(3, 1)

        self.s.start()

    def start(self, s):
        self.strings[s].out()

    def stop(self, s):
        self.strings[s].stop()

    def fret(self, s, num):
        self.freq(s, self.OPEN[s] * (2.**(1./12.))**num)

    def freq(self, s, hz):
        print("String {} to {} hz".format(s, hz))
        self.strings[s].freq = hz
