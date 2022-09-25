import scrython

print("Testing out scrython")

card = scrython.cards.Named(fuzzy="Black Lotus")

print(card.name())
print(card.id())
print(card.oracle_text())
