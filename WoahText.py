import os 
import time

def mainprogram():
  print('''
   
 
    \__/  \__/      \______/  /__/     \__\ |__|  |__|                                                 
   ''')
  time.sleep(1)
  os.system('clear')
  print(''' 

 
   \    /\    /    |  `--'  |  /  _____  \  |  |  |  | 
    \__/  \__/      \______/  /__/     \__\ |__|  |__| 
   ''')
  time.sleep(1)
  os.system('clear')
  print(''' 
    
 
  \            /   |  |  |  |   /  /_\  \   |   __   | 
   \    /\    /    |  `--'  |  /  _____  \  |  |  |  | 
    \__/  \__/      \______/  /__/     \__\ |__|  |__| 
                                                       
  
  ''')
  time.sleep(1)
  os.system('clear')
  print(''' 
  

 \   \/    \/   /  |  |  |  |    /  ^  \    |  |__|  | 
  \            /   |  |  |  |   /  /_\  \   |   __   | 
   \    /\    /    |  `--'  |  /  _____  \  |  |  |  | 
    \__/  \__/      \______/  /__/     \__\ |__|  |__| 
 
    ''')
  time.sleep(1)
  os.system('clear')
  print('''
    
\   \  /  \  /   /  /  __  \      /   \     |  |  |  | 
 \   \/    \/   /  |  |  |  |    /  ^  \    |  |__|  | 
  \            /   |  |  |  |   /  /_\  \   |   __   | 
   \    /\    /    |  `--'  |  /  _____  \  |  |  |  | 
    \__/  \__/      \______/  /__/     \__\ |__|  |__| 
                                                        
    ''')
  
def startprogram():
  start = input('Start?: ')
  if str(start):
    os.system('clear')
    mainprogram()
  else:
    os.system('clear')
    startprogram()



startprogram()
