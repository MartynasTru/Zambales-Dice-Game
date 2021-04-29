#Program Name: Coursework 2
#Program Author: 19019021

import random


def Greetings():
    """
    Prints out welcoming lines and gets player name 
    - - - -
    Returns players name
    """
    print("====================\n")
    print("Welcome to Zambales!\n")
    print("====================\n")
    #convert name to string if user chooses his name as numbers or char variables
    name = str(input("Enter your name: "))
    print("Greetings ", name) 
    print("Roll the die 5 times, see if you can throw a double.\n")
    return name

def gameStatus(name):
    """
    This function checks wether player wants to play or no
    - - - -
    Returns true (if player wants to play) or false (if player does not want to play)
    """
    print(name, ", do you want to play the game (y/n)? ", end="")
    answer = str(input())
    print("\n")
    #checking only for 'y' and 'Y', otherwise stopping the game
    if ((answer == 'y') or (answer == 'Y')):
        print("PLAYING!!!\n")
        return True
    else:
        return False
        pass

def DiceRoll():
    """
    This function generates random zambales symbol
    - - - -
    Return value of randomRoll
    """
    #rolling dice using zambales charcaters
    randomRoll = random.choice(['I', 'II', 'III', 'X', '+', '#'])
    return randomRoll

def DiceOutput(ifPlaying, name):
    """
    Function that compares zambales symbols, prints them out and tracks all the results
    - - - -
    status - true or false, depending on whether player wants to play
    gamesPlayed - how many games player has played
    gamesWon - how many games player has won
    inGameDoubleCounter - how many doubles player rolled in one seperate game
    totalDoubleCounter - how many doubles player has had throughout all games
    """
    status = ifPlaying
    gamesPlayed = 0
    gamesWon = 0
    inGameDoubleCounter = 0 #variable for seperate game doubles
    totalDoubleCounter = 0 #variable for total doubles throughout all games
    while(status):
        doublesCounter = 0
        gamesPlayed+=1
        print("Game ", gamesPlayed)
        for counter in range(5):
            # putting random dice roll into variables for further comparison
            firstRoll = DiceRoll()
            secondRoll = DiceRoll()
            #checking for doubles before printing in order to print it in one line 
            if(firstRoll == secondRoll):
                print("[", counter+1, "] " ,firstRoll, ",", secondRoll, end = '')
                print(" -- double")
                doublesCounter += 1
            else:
                print("[", counter+1, "] " ,firstRoll, ",", secondRoll)
        print("\n")
        if (doublesCounter==1):
            print(doublesCounter, " double\n")
        else:
            print(doublesCounter, " doubles\n")
        #checking whether the game was won 
        if(doublesCounter>0):
                gamesWon += 1
        totalDoubleCounter += doublesCounter
        status = gameStatus(name)
    Results(gamesPlayed, gamesWon, totalDoubleCounter, name)
    
def Results(totalGamesPlayed, totalGamesWon, totalDoubles, name):
    """
    Prints out all the results collected in DiceOutput function
    """
    #printing out the results once the game has ended
    print("Results:")
    print("========")
    print("Total number of games: " ,totalGamesPlayed)
    print("Total games won: ", totalGamesWon)
    print("Total doubles: " ,totalDoubles)
    print("Average doubles per game: " ,round(totalDoubles/totalGamesPlayed,2))
    print("\n") #skipping one line
    print("Bye, bye ", name)


def main():
    #calling the functions
    name = Greetings()
    ifPlaying = gameStatus(name)
    DiceOutput(ifPlaying, name)

if __name__ == "__main__":
    main()
    pass