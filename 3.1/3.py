L = int(input())
N = int(input())
for i in range(N):
    word = input()
    if len(word) > L:
        print(word[:(L - 3)] + "...")
    else:
        print(word)
