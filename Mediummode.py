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

questions = ["What kind of chemical element hates to be a follower?","What did the chemistry teacher do with his dead pet?","What is the loneliest of all physics concepts?","What would you call a re-make of the classic film Tron?","Which weighs more a ton of concrete or a ton of feathers?\n A) A ton of concrete\n B) A ton of feathers\n C) They both weigh a ton"]
answers = ["lead","barium","singularity","neutron","C"]
result = []

for x in questions:
  ask = input("\n" + color.BOLD + color.CYAN + x + "\n" + color.END)
  result.append(ask)

if result == answers:
  print(color.BOLD, color.GREEN + "You got all your answers right!" + color.END)
else:
  print(color.BOLD, color.RED + "You got some questions wrong!" + color.END)
  exit()