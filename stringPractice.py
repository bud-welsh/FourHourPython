print("Good Times") # A regular string

print("A\nnew\nline") # A new line

print("\"Escaping quotes\"")

phrase = "This string comes from the variable \"phrase\"."
print(phrase)
print(phrase + "\nThis string comes from concatenation.")

print(phrase.lower()) # Make phrase all lower case letters
print(phrase.upper()) # Make phrase all upper case letters

print(len(phrase)) # checking the length of the phrase

print(phrase[0]) # printing the first letter of the phrase
print(phrase[3]) # printing the fourth letter of the phrase

print(phrase.index("m")) # find the index of the letter m in the phrase
print(phrase.index("the")) # find the starting index of the word the in the phrase
