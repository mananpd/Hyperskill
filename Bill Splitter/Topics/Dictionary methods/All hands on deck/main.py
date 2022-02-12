cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10",  "Jack", "Queen", "King", "Ace"]
dic_cards = {}
for value in range(2,15):
    dic_cards[cards[value - 2]] = value
card_sum = 0
for _ in range(6):
    card_sum += dic_cards[input()]
print(card_sum/6)
