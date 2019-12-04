message=input(">")
words=message.split(' ')
print(words)
emojis={
    ":)":"happy face",
    ":(":"sad face"
}
output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)
