import random

with open("characters.txt", "r", encoding="utf-8") as file:
    characters = file.readlines()

with open("output.txt", "w", encoding="utf-8") as file2:
    for name in characters:
        status = random.choice(["alive", "dead"])
        print(name.strip(), "-", status)
        file2.write(f"{name.strip()} – {status}\n")
        
alive = []
dead = []

with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "alive" in line:
            alive.append(line)
        elif "dead" in line:
            dead.append(line)

with open("alive-characters.txt", "w", encoding="utf-8") as file_alive:
    file_alive.writelines(alive)

with open("dead-characters.txt", "w", encoding="utf-8") as file_dead:
    file_dead.writelines(dead)