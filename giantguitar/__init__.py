#!/usr/bin/python
import sys
import os
import time
import signal
import atexit
import random
import numpy
from Queue import Queue
from itertools import cycle
from optparse import OptionParser



# mine
from sounder import Sounder
from player import Player



q = {}

def get_str(ch):
  return 6 - ch

def main(opts):
  if not opts.demo:
    from reader import Reader

  global q
  delay = .001
  lights = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

  print opts
  if not opts.demo:
    reader = Reader(lights)

  sounder = Sounder()
  player = Player(sounder)
  songs = os.listdir("./songs/")
  songs = filter(lambda x: x.endswith('.js'), songs)

  numpy.random.shuffle(songs)
  print("Loaded songs:")
  print(songs)

  for song in cycle(songs):
    # time.sleep(.5)
    q = player.song(song)

    while True:
      debug_str = ""
      time.sleep(delay)

      if not opts.demo:
        reader.fetch()

      if not q["play"].empty():
        player.chord(q["play"].get_nowait())

      for ch in lights:
        debug_str += "{}:{} ".format(ch, lights[ch])
        if lights[ch] < 650 or opts.demo:
          sounder.start(get_str(ch))
        else:
          sounder.stop(get_str(ch))

      # print(debug_str)
      time.sleep(delay)

      if q["sig"] == "stopped":
        print "caught sig... stopping song"
        sounder.mute()
        break

def sig_handler(sig, frame):
  cleanup()

def cleanup():
  print("\n\nShutting Giant Guitar with Fricken Laser Beams down...\n\n")
  q["control"].put("stop")
  sys.exit(0)

if __name__ == "__main__":
  parser = OptionParser()
  parser.add_option("-d", "--demo", dest="demo", action="store_true", default=False)
  (options, args) = parser.parse_args()
  signal.signal(signal.SIGINT, sig_handler)
  atexit.register(cleanup)
  main(options)
