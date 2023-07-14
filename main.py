import random

def rollDice(noofSides):
  result = random.randint(1, noofSides)
  return result


def rollDices():
  rollFirstDice = rollDice(6)
  rollSecondDice = rollDice(8)
  health = rollFirstDice * rollSecondDice
  return health
  
print("⚔️ Character Stats Generator ⚔️")

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(rollDices())
  print("Their health is  ", health,"hp")
  haveACharacter = input("Want to create another character? ")
  