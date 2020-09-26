import colorama

colorama.init() # init colored terminal

# constants
RED   = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
BLUE  = colorama.Fore.BLUE
RESET = colorama.Style.RESET_ALL

BANNERS = [
"""
  ::::::::::::...    ::::::::::..    :::  .     :::.    :::::::..    :::. ::::::::::::
;;;;;;;;'''';;     ;;;;;;;``;;;;   ;;; .;;,.  ;;`;;   ;;;;``;;;;   ;;`;;;;;;;;;;''''
     [[    [['     [[[ [[[,/[[['   [[[[[/'   ,[[ '[[,  [[[,/[[['  ,[[ '[[,   [[     
     $$    $$      $$$ $$$$$$c    _$$$$,ccccc$$$cc$$$c $$$$$$c   c$$$cc$$$c  $$     
     88,   88    .d888 888b "88bo,"888"88o,  888   888,888b "88bo,888   888, 88,    
     MMM    "YmmMMMM"" MMMM   "W"  MMM "MMP" YMM   ""` MMMM   "W" YMM   ""`  MMM    

    @alismsk234, @n30phyt3
""",
"""
 _____           _           _              _   
|_   _|   _ _ __| | __      / \   _ __ __ _| |_ 
  | || | | | '__| |/ /____ / _ \ | '__/ _` | __|
  | || |_| | |  |   <_____/ ___ \| | | (_| | |_ 
  |_| \__,_|_|  |_|\_\   /_/   \_\_|  \__,_|\__|
                                                
    @alismsk234, @n30phyt3
"""
]

def print_banner():
  from random import choice
  print(choice(BANNERS))
  return

def print_color(color, *args):
  print(color, sep="", end="") # begin style
  print(*args, sep="", end="") # print text
  print(RESET, sep="", end="") # reset style
  return
