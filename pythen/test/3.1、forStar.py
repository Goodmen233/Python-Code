row = 5
for i in range(1, row + 1):
    count = 2 * i - 1
    for j in range(2 * row - count - 1):
        print(" ", end="")
    for k in range(count):
        print("* ", end="")
    print("")
