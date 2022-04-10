import math

NUMBER_OF_PRIME=50
NUMBER_OF_LINE_PRIME=10
number = 2
count = 0
while count < NUMBER_OF_PRIME:
    isPrime = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            isPrime = 0
            break
    if isPrime == 1:
        print(number, end="\t")
        count = count + 1
        if count % NUMBER_OF_LINE_PRIME == 0:
            print()
    number = number + 1



