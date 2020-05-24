from poker.hand import Hand
from poker.poker import score

with open('poker.txt') as f:
    games = f.read().splitlines()
    count = 0
    for line in games:
        game = line.split(" ")
        hand_one = Hand(game[0:5])
        hand_two = Hand(game[5:10])
        if score(hand_one, hand_two) == 'Player 1':
            count += 1
    print(count)
