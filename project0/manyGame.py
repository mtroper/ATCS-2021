games = ["minecraft", "portal", "clash of clans", "chess"]
print("I play", end=" ")
for game in games:
    print(game, end=" ")
print()
while(True):
    games.append(input("What game do you like?\n"))
    print("We play", end=" ")
    for game in games:
        print(game, end=" ")
    print()