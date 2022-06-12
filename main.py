from math import trunc
from random import randint
score = 0
numWrong = 0

def titleScreen():
    choice = input("Hello! Would you like to test your knowledge of the day of any given new year? (Y/N)")
    if choice == "Y":
        print("Ok, let's get started")
    elif choice == "N":
        print("Too bad, you are playing anyway")
    print("--------------------------------------------------------------------")
    print("The rules are simple:")
    print("A random year will appear, and you need to guess which day of the week the new year (January 1st) falls on")
    print("You will get a point if you get it right, but 0 points if you get it wrong")
    print("Careful, you only have 3 strikes before the game ends. Try to get the highest score!")
    startGame()

def startGame():
    global score
    global numWrong

    while numWrong < 3:
        year = randint(1582, 3000)
        dayOfWeek = (year * 365 + trunc((year - 1) / 4) - trunc((year - 1) / 100) + trunc((year - 1) / 400)) % 7

        if dayOfWeek == 0:
            dayOfWeekName = "Sunday"
        elif dayOfWeek == 1:
            dayOfWeekName = "Monday"
        elif dayOfWeek == 2:
            dayOfWeekName = "Tuesday"
        elif dayOfWeek == 3:
            dayOfWeekName = "Wednesday"
        elif dayOfWeek == 4:
            dayOfWeekName = "Thursday"
        elif dayOfWeek == 5:
            dayOfWeekName = "Friday"
        elif dayOfWeek == 6:
            dayOfWeekName = "Saturday"

        print("--------------------------------------------------------------------")
        userInput = input("The year is " + str(year) + ", on what day does the new year fall on?  (M/T/W/Th/F/S/Su")
        if userInput == "Su" and dayOfWeek == 0:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "M" and dayOfWeek == 1:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "T" and dayOfWeek == 2:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "W" and dayOfWeek == 3:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "Th" and dayOfWeek == 4:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "F" and dayOfWeek == 5:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        elif userInput == "S" and dayOfWeek == 6:
            score+= 1
            print("That is correct!")
            print("Your score is " + str(score))
        else:
            numWrong+= 1
            print("That is incorrect. The correct day is " + dayOfWeekName)
            print("You have " + str(numWrong) + " strike(s)")
    print("--------------------------------------------------------------------")
    playAgain = input("Game Over: Your Score was: " + str(score) + ". Play again? (Y/N)")
    if playAgain == "Y":
        startGame()

titleScreen()
