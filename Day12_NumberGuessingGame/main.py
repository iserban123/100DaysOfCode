from asci import logo
import random

def difficulty(level):
  if level == "hard":
    return 5
  else:
    return 10

def compare(player_no, computer_no):
  if player_no > computer_no:
    print("Number to high")
  else:
    print("Number to low")


print(logo)
print("Welcome to the game!")
level = input("Choose difficulty: easy or hard ")
computer_no = random.randint(1,101)
print(f"computer no:{computer_no}")
game_over = False
lives = difficulty(level)
lives_remaining = lives

while not game_over:
   player_no = int(input("Choose a number between 1-100:"))
   
   if lives_remaining > 0 and player_no != computer_no:
    print(f"Lives remaining: {lives_remaining}")
    compare(player_no,computer_no)
    lives_remaining = lives_remaining - 1
   elif lives_remaining > 0 and player_no == computer_no:
     print("You won!")
     game_over = True
   else:
     print("You lost!")
     game_over = True







