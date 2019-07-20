highscores=[45, 67, 56, 78]
for i,b in enumerate(highscores) :
    print(i + 1,b, sep=".")
while True:
    
    a=int(input("New highscore: "))
    highscores.append(a)
    highscores.sort(reverse=True)
    for i,b in enumerate(highscores):
        if i < 5:
            print(i+1,b,sep='.')