row = 8
for i in range(1, row + 1):
    count = 2 * i - 1
    for j in range(2 * row - count - 1):
        print("\t", end="")
    for l in range(0, i):
        print("{}\t\t".format(2**l), end="")
    for m in range(1, i):
        print("{}\t\t".format(2**(i-m-1)), end="")
    print("")
