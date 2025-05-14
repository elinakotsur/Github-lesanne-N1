from colorama import Fore, Style,Back
import emoji
     


print(Back.CYAN +"Hello")
mood=input("What is your mood now???(happy,sad,tired,shocked)")

moods = {
    "happy": {
        "font": Fore.BLACK,
        "bg": Back.YELLOW,
        "text": "You are happy right now!",
        "enoji": emoji.emojize(':thumbs_up:')
    },
    "sad": {
        "font": Fore.WHITE,
        "bg": Back.BLUE,
        "text": "You are sad right now",
        "enoji": emoji.emojize(':disappointed_face:')
    },
    "tired": {
        "font": Fore.BLACK,
        "bg": Back.GREEN,
        "text": "You are tirda right now",
        "enoji": emoji.emojize(':sleeping_face:')
    },
    "shocked": {
        "font": Fore.WHITE,
        "bg": Back.MAGENTA,
        "text": "You are shocked right now",
        "enoji": emoji.emojize(':fearful_face:')
    }
}


if mood in moods:
    m = moods[mood]
    print(m["bg"] + m["font"] +  " " + m["text"]+" " + m["enoji"] )

else:
    print(Fore.RED + "Something was wrong")