from game_data import data
import random
from art import logo, vs
from replit import clear


def personal_data():
 person = random.choice(data)
 return person


def sentence(per):
 name = per["name"]
 description = per["description"]
 country = per["country"]
 return f"{name}, a {description}, from {country}"


def compare(answer, person1, person2):
  clear()
  print(logo)
  global play
  f1 = person1["follower_count"]
  f2 = person2["follower_count"]
  if (answer == "A" and f1 > f2) or (answer == "B" and f2 > f1):
     
     print(f"Well done")
     return 1   
  else:
     clear()
     print(logo)
     play = False
     print("You lose!") 


def game():
  print(logo)
  person1 = personal_data() 
  sent1 = sentence(per=person1)
  followers1 = person1["follower_count"]
  score = 0

  while play:
    person2 = personal_data()
    sent2 = sentence(per=person2)
    followers2 = person2["follower_count"]
    
    while person1 == person2:
      person2 = personal_data()
    
    print(f"Compare A: {sent1}")
    print(vs)
    print(f"Against B: {sent2}")
    answer = input("Who has more followers?Type 'A' or 'B':").upper()


    ct = compare(answer,person1,person2)
    if ct == 1:
      score = score + 1
    print(f"Score:{score}")
    person1 = person2
    sent1 = sent2


play = True
game()
