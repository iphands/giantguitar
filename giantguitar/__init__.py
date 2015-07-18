#!/usr/bin/python

import os
import time
from reader import Reader 
from player import Player

def main():
  delay = .03
  lights = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

  reader = Reader(lights)  
  player = Player()
  
  while True:
    time.sleep(delay)
    reader.fetch()
    os.system('clear')

    for ch in lights:
      if lights[ch] < 300:
        player.stop(ch+1)
      else:
        player.start(ch+1)

      print("{}: {}".format(ch, lights[ch]))
    print("--------------------------------------------")
    time.sleep(delay)
              
if __name__ == "__main__":
  main()

