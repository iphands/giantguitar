#!/usr/bin/python

import os
import time
from Queue import Queue

from reader import Reader 
from sounder import Sounder
from player import Player

def main():
  delay = .1
  lights = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

  reader = Reader(lights)  
  sounder = Sounder()
  player = Player(sounder)
  q = player.song("polly")

  while True:
    time.sleep(delay)
    reader.fetch()
    #os.system('clear')
    
    if not q.empty():
      player.chord(q.get_nowait())

    for ch in lights:
      if lights[ch] > 3 or ch == 4:
        sounder.start(ch+1)
      else:
        sounder.stop(ch+1)
      #print("{}: {}".format(ch, lights[ch]))
    #print("--------------------------------------------")
    time.sleep(delay)
              
if __name__ == "__main__":
  main()

