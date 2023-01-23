def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": "☺",  #windows key + ; for emojis
        ":(": "😞"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


input_message = input(">")
print(emoji_converter(input_message))

