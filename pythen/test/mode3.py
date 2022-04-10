for i in range(1,7):
    for j in range(6 - i):
        print(end="  ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
