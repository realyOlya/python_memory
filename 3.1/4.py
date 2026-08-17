while (word := input()) != "":
    if not word.endswith("@@@"):
        word = word.lstrip("##")
        print(word)
