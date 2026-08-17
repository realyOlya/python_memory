let = []
counts = []

while (word := input()) != "ФИНИШ":
    word = word.lower()
    for letter in word:
        if not letter.isalpha():
            continue
        if letter in let:
            index = let.index(letter)
            counts[index] += 1
        else:
            let.append(letter)
            counts.append(1)

max_count = max(counts)
best = None

for i in range(len(let)):
    if counts[i] == max_count:
        if best is None or let[i] < best:
            best = let[i]

print(best)
