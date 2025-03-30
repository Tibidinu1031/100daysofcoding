import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play(loops=-1)

def pause():
  pygame.mixer.pause()

pause()
print("MyPod Music Player")
print()
def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    print("Press 1 to Play")
    time.sleep(3)
    os.system("clear")
    print("Press 2 to Pause")
    time.sleep(3)
    os.system("clear")
    print("Press 3 to see the menu again")
    time.sleep(3)
    os.system("clear")
    print("Press anything else to exit")
    time.sleep(3)
    os.system("clear")
    choice = input("Please enter your choice: ")
    if choice == "1":
      print("\033[0;32mPlaying some proper tunes!\033[0m")
      play()
    elif choice == "2":
      print("\033[0;33mPausing the music!\033[0m")
      pause()
    elif choice == "3":
      print("\033[0;34mRepeating the menu!\033[0m")
      continue
    else:
      print("\033[0;31mThank you for using MyPod Music Player\033[0m")
      exit()
    

while True:
  
  if True:
    play()