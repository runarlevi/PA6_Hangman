import csv
import random
fileStream = open("words.txt", "r")
wordBank = fileStream.read().split("\n")
fileStream.close()

class Hangman:
    def __init__(self, name="Unknown", wins=0, losses=0):
        self.name = name
        self.wins = wins
        self.losses = losses

    def __str__(self):
        pass

    def start(self):
        play = input("Press 'a' to play, any other key to quit: ")

        while play == "a":
            wrongGuesses = 0
            GUESSES = self.getGuesses()
            theWord, unclearWord = self.chooseWord()

            print("\nA word has been chosen for you: " + " ".join(unclearWord))
            print("You have a total of " + str(GUESSES) + " guesses.")

            while True:
                userInput = input("Try to guess a letter or the whole word: ")
                print()

                if len(userInput.strip()) > 1:
                    if self.wordCorrect(theWord, userInput.strip()):
                        unclearWord = theWord
                        self.printResults(theWord, unclearWord, GUESSES)
                        self.storeSores(theWord, wrongGuesses, GUESSES)
                        break

                if userInput.strip() in theWord:
                    print("Right guess!")
                    self.correctGuess(theWord, unclearWord, userInput.strip())

                else:
                    wrongGuesses += 1
                    GUESSES -= 1
                    print("Wrong guess.")

                if self.gameOver(theWord, unclearWord, GUESSES):
                    self.printResults(theWord, unclearWord, GUESSES)
                    self.storeSores(theWord, wrongGuesses, GUESSES)
                    break

                print("You have " + str(GUESSES) + " guesses left.\n")
                print("The word: " + " ".join(unclearWord))

            play = input("Press 'a' to play again, any other key to quit: ")

    def getGuesses(self):
        while True:
            retVal = int(input("How many guesses do you want? "))
            if retVal > 0:
                return retVal
            print("Has to be a positive number.")


    def chooseWord(self):
        randomIndex = random.randint(0, len(wordBank))
        theWord = list(wordBank[randomIndex])
        unclearWord = ["-"] * len(theWord)
        print(theWord)
        return theWord, unclearWord

    def gameOver(self, theWord, unclearWord, GUESSES):
        if theWord == unclearWord:
            self.wins += 1
            return True
        if GUESSES == 0:
            self.losses += 1
            return True
        return False

    def printResults(self, theWord, unclearWord, GUESSES):
        if theWord == unclearWord:
            print("*** Congratulations you won! ***\nThe word was: " + "".join(theWord))
            print("You have " + str(self.wins) + " wins and " + str(self.losses) + " losses this run!")
            print()
            return
        if GUESSES == 0:
            print("... You lost ...\nThe word was: " + "".join(theWord))
            print("You have " + str(self.wins) + " wins and " + str(self.losses) + " losses this run!")
            print()
            return

    def correctGuess(self, theWord, unclearWord, userInput):
        for index, value in enumerate(theWord):
            if value == userInput:
                unclearWord[index] = theWord[index]

    def wordCorrect(self, theWord, userInput):
        if list(userInput) == theWord:
            self.wins += 1
            return True
        return False

    def storeSores(self, theWord, wrongGuesses, GUESSES):
        with open('scores.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if wrongGuesses == GUESSES:
                writer.writerow([self.name, "".join(theWord), wrongGuesses, "Loss"])
            else:
                writer.writerow([self.name, "".join(theWord), wrongGuesses, "Win"])
