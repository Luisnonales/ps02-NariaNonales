sentence = "Python is fun anf Python is easy to learn!"

for letter in sentence:
    if letter in "aeiou":
        print(letter.upper(), end="")

    else:
        print(letter, end="")
        