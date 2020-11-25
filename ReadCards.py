# Read Cards and Top Card
def readcards(AllHands, Player, TopCard):
    readcards4(AllHands, Player)
    print("Top Card: " + str(FaceCards(TopCard[0])) + " of " + str(TopCard[1]))


# Read Cards and new Card
def readcards2(AllHands, Player, NewCard):
    readcards4(AllHands, Player)
    print("8) New Card: " + str(FaceCards(NewCard[0])) + " of " + str(NewCard[1]))


# Read Cards for first hand
def readcards3(AllHands, Player):
    readcards4(AllHands, Player)
    CardNumber = FaceCards(AllHands[Player][7][0])
    CardType = AllHands[Player][7][1]
    print("8) " + str(CardNumber) + " of " + str(CardType))


# Read cards 1-7 (base function/Win Condition)
def readcards4(AllHands, Player):
    print("Player " + str(Player + 1) + " Has: \n")
    CardNumber = FaceCards(AllHands[Player][0][0])
    CardType = AllHands[Player][0][1]
    print("1) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][1][0])
    CardType = AllHands[Player][1][1]
    print("2) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][2][0])
    CardType = AllHands[Player][2][1]
    print("3) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][3][0])
    CardType = AllHands[Player][3][1]
    print("4) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][4][0])
    CardType = AllHands[Player][4][1]
    print("5) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][5][0])
    CardType = AllHands[Player][5][1]
    print("6) " + str(CardNumber) + " of " + str(CardType))
    CardNumber = FaceCards(AllHands[Player][6][0])
    CardType = AllHands[Player][6][1]
    print("7) " + str(CardNumber) + " of " + str(CardType))


def FaceCards(CardNumber):
    if CardNumber == 1:
        return "Ace"
    elif 2 <= CardNumber <= 10:
        return CardNumber
    elif CardNumber == 11:
        return "Jack"
    elif CardNumber == 12:
        return "Queen"
    elif CardNumber == 13:
        return "King"


def WinCondition(PlayersHand):
    Numbers = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0],
               [13, 0]]
    SuitKey = {
        0: "Hearts",
        1: "Spades",
        2: "Clubs",
        3: "Diamonds"
    }
    Suits = [[],[], [], []]
    WinSet = []
    WinRun = []
    Set = 0
    Run = 0
    for Card in range(8):
        Numbers[PlayersHand[Card][0]-1][1] = Numbers[PlayersHand[Card][0]-1][1] + 1
        if PlayersHand[Card][1] == "Hearts":
            Suits[0].append(PlayersHand[Card][0])
        if PlayersHand[Card][1] == "Spades":
            Suits[1].append(PlayersHand[Card][0])
        if PlayersHand[Card][1] == "Clubs":
            Suits[2].append(PlayersHand[Card][0])
        if PlayersHand[Card][1] == "Diamonds":
            Suits[3].append(PlayersHand[Card][0])
    for Number in range(13):
        if Numbers[Number][1] >= 3:
            Set = Set + 1
            WinSet.append(Number + 1)
    for suit in range(4):
        Suits[suit].sort()
        Numbers = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0],
                   [13, 0]]
        for card in range(len(Suits[suit])):
           number = Suits[suit][card]-1
           Numbers[number][1] = 1
        for list in range(1,12):
            if Numbers[list-1][1] + Numbers[list][1] + Numbers[list+1][1] == 3:
                Run = Run + 1
                WinRun.append(str(list-1) + " " + str(list) + " " + str(list+1) + " of " + SuitKey[suit])
    if Set + Run == 2:
        return True
    else:
        False


