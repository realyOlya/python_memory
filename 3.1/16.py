line = input()
line_without_all = line.lower().replace(" ", "")
if line_without_all == line_without_all[::-1]:
    print("YES")
else:
    print("NO")
