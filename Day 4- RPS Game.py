import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

guess = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
list  = [rock,paper,scissors]
human = list[guess]
machine = random.choice(list)

print (f"you picked {human}")
print (f"machine picked {machine}")

if human == 'rock' and machine == 'scissors':
  print ('You won!')

elif human == 'paper' and machine == 'rock':
  print ('You won!')

elif human == 'scissors' and machine == 'paper':
  print ('You won!')

elif human == machine:
  print ("Draw!")

else:
  print("You Loose!")
