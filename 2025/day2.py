def readFile(file):
    f = open(file, "r")
    lines = f.read().replace("\n","")

    ranges = lines.split(",")
    
    ranges = [tuple(rng.split("-")) for rng in ranges]

    return ranges 


FILE = "day2_input.txt"
ranges = readFile(FILE)

def partOne(moves):
    count = 0
    for rng in ranges:
        x, y = rng
        for i in range(int(x), int(y)+1):
            num = str(i)
            if len(num) % 2 == 0:
                mid = len(num) // 2
                if num[:mid] == num[mid:]:
                    count += i

    return count


import re

def works(num: str):
    pattern = r"^(.+)\1+$"
    
    match = re.match(pattern, num)
    
    return bool(match)


def partTwo(moves):
    # create a map 
    count = 0
    for rng in ranges:
        x, y = rng
        for i in range(int(x), int(y)+1):
            num = str(i)
            if len(num) > 1:
                count += i if works(num) else 0
            
    return count 

print(partTwo(ranges))
