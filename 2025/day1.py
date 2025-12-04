def readFile(file):
    f = open(file, "r")
    lines = f.readlines()
    
    lines = [line.replace("\n", "") for line in lines]
    return lines

FILE = "day1_input.txt"
moves = readFile(FILE)

def partOne(moves):
    current = 50 # this was given
    count = 0
    for move in moves:
        if move[0] == "L":
            current = (current - int(move[1:])) % 100
        elif move[0] == "R":
            current = (current + int(move[1:])) % 100
        
        count += 1 if current == 0 else 0

    return count

def partTwo(moves):
    current = 50 # this was given
    count = 0
    n = 0
    for move in moves:
        value = int(move[1:])
        if move[0] == "L":
            n -= value
            count += abs((n%100)//100 - current//100)
        elif move[0] == "R":
            n += value
            count += abs(n//100 - current//100)
        current = n % 100
        count += 1 if current == 0 else 0
    return count

def part2(moves, start=50, dial_size=100):
    pos = start     # current dial position in [0..dial_size-1]
    count = 0
    unwrapped = start   # track “absolute” position before modulo

    for instr in moves:
        steps = int(instr[1:])
        if instr[0] == 'R':
            unwrapped += steps
            count += unwrapped // dial_size - ( (unwrapped - steps) // dial_size )
        else:  # 'L'
            unwrapped -= steps
            # When moving left, crossing zero corresponds to going past a multiple of dial_size downward
            # Compute how many multiples of dial_size we passed
            prev_cycle = (unwrapped + steps + (dial_size - 1)) // dial_size
            new_cycle = (unwrapped + (dial_size - 1)) // dial_size
            count += prev_cycle - new_cycle

        pos = unwrapped % dial_size
        # If we ended exactly on 0, that landing is already counted by the wrap logic above

    return count

print(part2(moves))
