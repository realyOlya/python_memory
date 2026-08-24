text = 'ехали медведи на велосипеде'
result = set(
    (sorted([word1, word2])[0], sorted([word1, word2])[1]) for word1 in text.split() for word2 in text.split() if
    word1 < word2 and len(set(word1) & set(word2)) >= 3)
print(result)
