def readFile(file):
    f = open(file, "r")
    lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    return lines


FILE = "day1_input.txt"
moves = readFile(FILE)


def partOne(moves):
    current = 50  # this was given
    count = 0
    for move in moves:
        if move[0] == "L":
            current = (current - int(move[1:])) % 100
        elif move[0] == "R":
            current = (current + int(move[1:])) % 100

        count += 1 if current == 0 else 0

    return count


def partTwo(moves):
    current = 50  # this was given
    count = 0
    # we keep a track of the number of cycles and don't normalize this
    for move in moves:
        value = int(move[1:])
        if move[0] == "L":
            prev = (current + 100 - 1) // 100
            current -= value
            # calculate number of cycles passed
            new = (current + 100 - 1) // 100

            count += prev - new
        elif move[0] == "R":
            prev = current // 100
            current += value
            count += current // 100 - prev

    return count


print(partTwo(moves))
