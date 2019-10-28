f = open("data.txt","r")
data = []
for line in f:
    data.append((line.strip()).split(" "))

player1wins = 0
player2wins = 0

def cardCount(hand):
    cardvalues = {}
    for card in hand:
        value = card[0]
        if value not in cardvalues:
            cardvalues[value] = 1
        else:
            cardvalues[value] += 1
    return cardvalues

def highestValue(hand):
    cardCounts = cardCount(hand)

def cardSort(values):
    pass


for hands in data:
    players = [hands[0:5], hands[5:10]]
    won = False
    #Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    print(cardCount(players[0]))
    break
    #Straight Flush: All cards are consecutive values of same suit.

    #Four of a Kind: Four cards of the same value.
    #Full House: Three of a kind and a pair.
    #Flush: All cards of the same suit.
    #Straight: All cards are consecutive values.
    #Three of a Kind: Three cards of the same value.
    #Two Pairs: Two different pairs.
    #One Pair: Two cards of the same value.
    #High Card: Highest value card.