# PA6 - Hangman - Egill & Rúnar
from PA6 import mainClass
import csv

def playHangman(players):
    for number, player in players.items():
        print(number, player)
    player = input("Please select one of the players above by typing a number: ")
    mainClass.Hangman(players[int(player)]).start()

def seeHistory(players):
    totalWrong = 0
    for number, player in players.items():
        print(number, player)
    player = input("Please select one of the players above by typing a number: ")
    games = getData(players, player)
    print("\nGames that " + players[int(player)] + " has played:")

    for i, j in games.items():
        totalWrong += int(j)
        print("Word: " + i + " - Wrong guesses: " + j)

    print("Total wrong guesses for " + players[int(player)] + ": " + str(totalWrong))
    print()

def addPlayer(players):
    newPlayer = input("New players name: ")
    players[len(players) + 1] = newPlayer
    print("A new player has been added!")

def getData(players, player):
    games = {}
    with open('scores.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)
        for line in csvReader:
            if line[0] == players[int(player)]:
                games[line[1]] = line[2]
    return games


players = {1: "Rúnar", 2: "Egill", 3: "Maggi", 4: "Trostan"}
selections = {1: "Play Hangman.", 2: "See history of scores.", 3: "Add player.", 4: "Quit."}

print("--- Welcome to Hangman! ---")
while True:
    print("You are now in the Main Menu.\n")
    for number, selection in selections.items():
        print(number, selection)
    print()

    choice = input("Please select one of the above by typing a number: ")
    if choice == "1":
        playHangman(players)
    elif choice == "2":
        seeHistory(players)
    elif choice == "3":
        addPlayer(players)
    elif choice == "4":
        print("--- Goodbye ---")
        break

