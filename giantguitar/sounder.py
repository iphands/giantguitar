from pyo import *
import random

class Sounder(object):
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
            string = self.strings[i] = {}
            string["state"] = False
            #string["lf2"] = Sine(freq=.15, mul=12, add=40, phase=round(random.uniform(0.1, 1.0), 10))
            #string["tone"] = Blit(self.OPEN[i], harms=3, mul=.3)
            #string["tone"] = Blit(self.OPEN[i], harms=string["lf2"], mul=.3)
            string["asdr"] = Adsr(attack=.05, decay=.3, sustain=.5, release=1, dur=0, mul=.5).play()
            string["tone"] = Sine(freq=self.OPEN[i], phase=round(random.uniform(0.1, 1.0), 10), mul=string["asdr"])
            string["chrs"] = Chorus(string["tone"], depth=.2, feedback=0.6, bal=0.06)
            #string["lfo"]  = Sine(freq=[.2,.25], mul=.5, add=.5)
            #string["harm"] = Harmonizer(self.strings[i]["tone"], transpo=12, winsize=0.05).out()
            #string["verb"] = Freeverb(self.strings[i]["tone"], size=[.79,.8], damp=.9, bal=.3).out()
            #string["dist"] = Disto(self.strings[i]["tone"], drive=.7, slope=.2, mul=.15).out()

        self.fret(5, 2)
        self.fret(4, 2)
        self.fret(3, 1)
        self.s.start()
        self.mute()

    def mute(self):
        print("MUTING")
        for i in range(1, 7):
            self.stop(i)

    def start(self, s):
        if not self.strings[s]["state"]:
            self.strings[s]["asdr"].play()
            self.strings[s]["chrs"].out()
            self.strings[s]["state"] = True

    def stop(self, s):
        if self.strings[s]["state"]:
            self.strings[s]["asdr"].stop()
            # self.strings[s]["tone"].stop()
            self.strings[s]["state"] = False

    def fret(self, s, num):
        self.freq(s, self.OPEN[s] * (2.**(1./12.))**num)

    def freq(self, s, hz):
        print("String {} to {} hz".format(s, hz))
        if self.strings[s]["state"]:
            self.strings[s]["asdr"].play()
        self.strings[s]["tone"].freq = hz
