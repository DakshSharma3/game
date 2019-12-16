import random
	 
# TO ADD NEW COLOR TO CLASS ADD: (COLOR VARIABLE NAME) = 'COLOR CODE'
class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
	  
print(color.BOLD, color.UNDERLINE, color.PURPLE+ "Welcome to Super cool dungeon master game!!!!\n" + color.END)

wisdom = random.randint(1,100)
charisma = random.randint(1,24)
powers = [wisdom, charisma]

stats = ["name:", "gender:", "age:"]
answers = []

for x in stats:
  ask = input("What is your " + color.BLUE + x + color.END + "\n")
  answers.append(ask)

stats.append("wisdom:")
stats.append("charisma:")
answers.extend(powers)

print(color.BOLD, color.UNDERLINE, color.PURPLE + "Player stats:\n" + color.END)

for i, (stats, answers) in enumerate(zip(stats, answers)):
  print(color.BLUE + stats + color.END, answers)
  
print(color.BOLD, color.UNDERLINE, color.PURPLE + "The objective of the game:\n" + color.END)

print("You're a prince and the princess have been taken by the villian called Skadooobedy!!!!!\n The aim of the game is to save the princess from Skadooobedy by answering questions.If you answer right you procced to the next level.\n If you save the princess you win but if you get a question wrong you lose.")
print( color.YELLOW +"Note that these will be multi choice question."+color.END) 