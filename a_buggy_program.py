def add_underscores(word):
    new_word = "_"
    for char in word:
        new_word = new_word + char + "_"
        print(f"Current character: {char}, New word: {new_word}")
    return new_word


phrase = "hello"
print(add_underscores(phrase))
