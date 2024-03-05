from random import randint as random_num
import os

print("Rock, Paper, Scissors:")

def pc_move():
  # Generate a random number between 1 and 60
  num = random_num(1, 60)
  # Return the corresponding move
  if num in range(1, 21):
    return 'rock'
  elif num in range(22, 41):
    return 'paper'
  else:
    return 'scissors'


while True:
  # Get the player's move
  player_output = (input("What is your move?: "))
  x = player_output.lower()
  y = pc_move()
  if x not in ['rock', 'paper', 'scissors']:
    os.system('cls||clear')
    print('Invalid move.')
    continue
  if y == x:
    print('Tie!')
    opt = input('Do you want to play again?: ')
    if opt == 'yes':
      os.system('cls||clear')
      continue
    else:
      print('Thanks for playing!')
      break
  elif (x == 'rock' and y == 'scissors') or (x == 'paper' and y == 'rock') or (x == 'scissors' and y == 'paper'):
    print("You win!")
    opt = input('Do you want to play again?: ')
    if opt == 'yes':
      os.system('cls||clear')
      continue
    else:
      print('Thanks for playing!')
      break
  else:
    print('Computer wins!')
    opt = input('Do you want to play again?: ')
    if opt == 'yes':
      os.system('cls||clear')
      continue
    else:
      print('Thanks for playing!')
      break
