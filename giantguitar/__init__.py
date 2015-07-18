#!/usr/bin/python

import os
import time
from reader import Reader 
from sounder import Sounder
from player import Player

def main():
  delay = .25
  lights = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

  reader = Reader(lights)  
  sounder = Sounder()
  player = Player(sounder)
  player.song("polly")
  i = 0



  while True:
    time.sleep(delay)
    reader.fetch()
    #os.system('clear')

    # if (i == 4):
    #   player.chord("a")

    # if (i == 8):
    #   player.chord("c")

    # if (i == 12):
    #   player.chord("f")


    # if (i > 18):
    #   player.chord("e")
    #   i = 0

    # i += 1

    for ch in lights:
      if lights[ch] > 333 or ch == 4:
        sounder.start(ch+1)
      else:
        sounder.stop(ch+1)
      #print("{}: {}".format(ch, lights[ch]))
    #print("--------------------------------------------")
    time.sleep(delay)
              
if __name__ == "__main__":
  main()

