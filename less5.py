with open("Game.txt","w") as file:
    file.write("hockey, tetris,football")
f = open("game.txt","rt")
list = []
for i in f:
    list.append(i)
    