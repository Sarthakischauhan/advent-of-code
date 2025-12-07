def readFile(file):
    f = open(file, "r")
    lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    return lines

FILE="test.txt"

numbers = readFile(FILE)

def partOne(numbers):
    total = 0
    for num in numbers:
        jolt = 0
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                jolt = max(jolt, int(num[i] + num[j]))
        total += jolt
    print(total)

def partTwo(numbers):
    big = ""
    
    for num in numbers:
        N = len(num)
        i, j = 0, N-1
        while (i + 12) < N and (j-12 > 0):


partTwo(numbers)
