

def readcards(AllHands, Player, TopCard):
    print("Player " + str(Player + 1) + " Has: \n")
    CardNumber = AllHands[Player][0][0]
    CardType = AllHands[Player][0][1]
    print("1) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][1][0]
    CardType = AllHands[Player][1][1]
    print("2) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][2][0]
    CardType = AllHands[Player][2][1]
    print("3) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][3][0]
    CardType = AllHands[Player][3][1]
    print("4) " + str(CardNumber) + " of " + str(CardType))
    print("Top Card: " + str(TopCard[0]) + " of " + str(TopCard[1]))

def readcards2(AllHands, Player, NewCard):
    print("Player " + str(Player + 1) + " Has: \n")
    CardNumber = AllHands[Player][0][0]
    CardType = AllHands[Player][0][1]
    print("1) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][1][0]
    CardType = AllHands[Player][1][1]
    print("2) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][2][0]
    CardType = AllHands[Player][2][1]
    print("3) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = AllHands[Player][3][0]
    CardType = AllHands[Player][3][1]
    print("4) " + str(CardNumber) + " of " + str(CardType))
    print("5) New Card: " + str(NewCard[0]) + " of " + str(NewCard[1]))