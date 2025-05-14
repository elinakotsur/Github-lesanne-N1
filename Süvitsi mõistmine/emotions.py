from colorama import init, Fore, Style,Back
import emoji
init()


print(Back.CYAN +"Hello")
mood=input("What is your mood now???(happy-1,sad-2,tired-3,shocked-4)")

if mood == 1:
    print(Back.YELLOW +Fore.RED+"you are happy now!!))")