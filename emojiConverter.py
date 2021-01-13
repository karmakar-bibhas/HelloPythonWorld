message = input(">")
words = message.split(' ')
emojis = {
    ":)": "happy",
    ":(": "Sad"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)