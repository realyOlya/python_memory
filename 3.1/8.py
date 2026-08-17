while (word := input()) != "":
    if not word.startswith("#"):
        if "#" in word:
            word = word[:word.find("#")]
        print(word)
