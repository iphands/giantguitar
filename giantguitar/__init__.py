#!/usr/bin/python

import os
import time
from reader import Reader 

def main():
  delay = .1
  lights = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
  reader = Reader(lights)  
  
  while True:
    time.sleep(delay)
    reader.fetch()
    os.system('clear')
    for ch in lights:
        print("{}: {}".format(ch, lights[ch]))
    print("--------------------------------------------")
    time.sleep(delay)
              
if __name__ == "__main__":
    main()
