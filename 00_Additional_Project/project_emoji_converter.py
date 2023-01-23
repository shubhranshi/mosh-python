message = input(">")
words = message.split(" ")
emoji = {
    ":)": "☺",  #windows key + ; for emojis
    ":(": "😞"
}
output_message = ""
for word in words:
    output_message += emoji.get(word, word) + " "
print(output_message)

