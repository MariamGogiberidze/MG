text = input("Type Something: ")
words = text.split( " ")
emojis = {
    ":)" : "😊",
    ":(" : "🙁",
    ":|" : "😐"
}

outcome = " "
for word in words:
    outcome += emojis.get(word, word) + " "
print(outcome)
