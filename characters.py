import random

with open("characters.txt", "r", encoding="utf-8") as file:
    characters = file.readlines()

with open("output.txt", "w", encoding="utf-8") as file2:
    for name in characters:
        status = random.choice(["alive", "dead"])
        print(name.strip(), "-", status)
        file2.write(f"{name.strip()} – {status}\n")
        
