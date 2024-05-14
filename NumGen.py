import random
import Main

maxRange = 1000
minRandom = Main.minRandom
maxRandom = Main.maxRandom

with open("Requests.txt", "w") as file:
    for _ in range(maxRange):
        file.write(str(random.randint(minRandom, maxRandom)) + "\n")

