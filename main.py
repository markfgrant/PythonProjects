import DeckOfCards
import random
import ReadCards

# Copy Tuple of Deck of Cards to list that I can use
CardList = list(DeckOfCards.Deck_Of_Cards)
# Allows the while function to run
PlayerEntry = True
while PlayerEntry:
    try:
        NumOfPlayers = int(input("Enter number of players (2-4): \n"))
        if 2 <= NumOfPlayers <= 4:
            function = True
            PlayerEntry = False
            print("Type p to play. Type q to quit.")
        else:
            print("Number of Players not acceptable. \n")
    except ValueError:
        print("Number of players not recognized")
        function = False

Players = [[], [], [], []]
if NumOfPlayers <4:
    Players.remove([])
    if NumOfPlayers <3:
        Players.remove([])

while function:
    # Exits if user types q
    UserInput = input()
    if UserInput == "q" or UserInput == "Q":
        function = False
        print("Have a nice day!")
    # Makes choice of random card if user does not quit
    elif UserInput == "p" or UserInput == "P":
        # Deal 7 cards to all players
        for Counter in range(7):
            for Player in range(NumOfPlayers):
                Card = random.choice(CardList)
                CardList.remove(Card)
                Players[Player].insert(0, Card)
        # Give 8th card to first player and make them discard
        Card = random.choice(CardList)
        CardList.remove(Card)
        Players[0].append(Card)
        ReadCards.readcards3(Players, 0)
        discard = Players[0][int(input("Please select which card you would like to discard (1-8)\n"))-1]
        Players[0].remove(discard)
        TopCard = discard
        NoWinner = True
        WhosTurn = 1
        DiscardPile = []
        while NoWinner:
            ReadCards.readcards(Players, WhosTurn, TopCard)
            PlayerChoice = input("Press t to take the top card or n to take a new card \n")
            if PlayerChoice == "t":
                Players[WhosTurn].append(TopCard)
                WinCondition = ReadCards.WinCondition(Players[WhosTurn])
                if WinCondition:
                    PlayerChoice = input("You have a win condition. Press W to win, or (1-7) to discard")
                    if PlayerChoice == "w" or PlayerChoice == "W":
                        print("Player " + str(WhosTurn) + " wins!")
                        ReadCards.readcards4(Players, WhosTurn)
                        NoWinner = False
                    else:
                        DiscardNum = int(PlayerChoice)
                else:
                    DiscardNum = int(input("Which Card would you like to discard? (1-7) \n"))
                Discard = Players[WhosTurn][DiscardNum-1]
                Players[WhosTurn].remove(Discard)
                TopCard = Discard
                if WhosTurn < NumOfPlayers-1:
                    WhosTurn += 1
                else:
                    WhosTurn = 0
            elif PlayerChoice == "n":
                if len(CardList) == 0:
                    function = False
                    NoWinner = False
                    print("Deck is out of Cards. Reshuffle will be added later. \n")
                else:
                    NewCard = random.choice(CardList)
                    CardList.remove(NewCard)
                    Players[WhosTurn].append(NewCard)
                    ReadCards.readcards2(Players, WhosTurn, NewCard)
                    WinCondition = ReadCards.WinCondition(Players[WhosTurn])
                    if WinCondition:
                        PlayerChoice = input("You have a win condition. Press W to win, or (1-7) to discard")
                        if PlayerChoice == "w" or PlayerChoice == "W":
                            print("Player " + str(WhosTurn) + " wins!")
                            ReadCards.readcards4(Players, WhosTurn)
                            NoWinner = False
                        else:
                            DiscardNum = int(PlayerChoice)
                    else:
                        DiscardNum = int(input("Which Card would you like to discard? (1-5) \n"))
                    Discard = Players[WhosTurn][DiscardNum-1]
                    Players[WhosTurn].remove(Discard)
                    DiscardPile.insert(0, TopCard)
                    TopCard = Discard
                    if WhosTurn < NumOfPlayers-1:
                        WhosTurn +=1
                    else:
                        WhosTurn = 0
    else:
        print("Please enter a valid operator")