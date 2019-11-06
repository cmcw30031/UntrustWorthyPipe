import random

money = 100

def slotmachine():
  global money
  slotchoice = ['$', '!', '7', 'BIG']
  slot1 = random.choice(slotchoice)
  slot2 = random.choice(slotchoice)
  slot3 = random.choice(slotchoice)
  print('''
 ''' + slot1 + '-' + slot2 + '-' + slot3 + '''
 ''')

  if slot1 == '$' and slot2 == '$' and slot3 == '$':
    print('You Win!')
    money += 1000
    print('+ $1000')
  elif slot1 == '!' and slot2 == '!' and slot3 == '!':
    print('You Win!')
    money += 1000
    print('+ $1000')
  elif slot1 == '7' and slot2 == '7' and slot3 == '7':
    print('You Win!')
    money += 1000
    print('+ $1000')
  elif slot1 == 'BIG' and slot2 == 'BIG' and slot3 == 'BIG':
    print('You Win!')
    money += 1000
    print('+ $1000')
  else:
      print('-100')
      money -= 100
def blankspace():
  print('')
start = ''

print('')

while start != 'stop':
  start = input('Go?:')
  blankspace()
  if str(start):  
    slotmachine()
  print('Balance: $' + str(money))
  blankspace()
