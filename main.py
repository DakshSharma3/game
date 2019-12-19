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

name = input(color.BLUE +"What is your name?" + color.END + "\n")

print(color.BOLD, color.UNDERLINE, color.PURPLE + "The objective of the game:\n" + color.END)

print("Hello", color.BLUE + name + color.END, "\nThe aim of the game is to help Shaun Donnelly save the princess from Bill Nye by answering science themed questions.\n If you get all the science questions right you win but if you get a question wrong you lose a chance. Once you have lost all your chances, you have lost the game!!\n\n")
print( color.YELLOW +"Note that there will be multi choice question.\n Put all lettered answers in capitals\n JUST ONES WITH INDIVIDUAL LETTERS NOT WORDS."+color.END) 

print (color.BOLD,color.UNDERLINE,color.GREEN + " Easy mode"+ color.END)
import Easymode
print (color.DARKCYAN,color.BOLD +"\n\nYou have gotten past bill's door and you're now trying to get past his guards\n\n"+ color.END)
print (color.BOLD,color.UNDERLINE,color.YELLOW + " Medium mode"+ color.END)
import Mediummode

print (color.DARKCYAN,color.BOLD +"You have defeated bill's guards and your are going head to head against bill nye to save your princess"+ color.END)
print (color.BOLD,color.UNDERLINE,color.RED + " Hard mode"+ color.END)
import hardmode
print("")
print("")
print("")

print(color.GREEN + " Thank you " + name + " for saving me from bill nye. You have my greatest gratitude" + color.END)

print(color.PURPLE + "Yes thank you , we couldnt of gotten her back without you"  + name + ". You also have my gratitude" + color.END)
print ("")
print("")
print(color.BOLD,color.RED,color.UNDERLINE + "Well done you have finished the game" + color.END)
print("")
print("")


exit = input("Press any key to exit:")
exit()