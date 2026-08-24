word1 = input().split(", ")
word2 = input().split(", ")
word3 = input().split(", ")
from itertools import chain

values = sorted(list(chain(word1, word2, word3)))
for index, value in enumerate(values, 1):
    print(f'{index}. {value}')
