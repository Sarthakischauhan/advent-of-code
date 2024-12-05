#! usr/bin/python3

# Rules for safe report
"""The levels are either all increasing or all decreasing."""
"""Any two adjacent levels differ by at least one and at most three"""

def part1():
    with open("puzzle2.txt", "r") as file:
        reports = file.readlines()
    file.close()

    count = 0
    for report in reports:
        report = report.replace("\n", "").split(" ")
        report = list(map(int, report))   
        
        prev = report[0]
        inc = True
        dec = True
        safe = True

        #1 4 5 8 11 12 9
        # to check whether they are increasing/decreasing
        for level in report[1:]:
            diff = level-prev
            if ( abs(diff) >= 1 and abs(diff) <= 3): 
                if ( diff > 0 ):
                    dec = False 
                if ( diff < 0 ):
                    inc = False
            else:
                safe = False
                break
            prev = level
        count += 1 if (safe and (inc or dec)) else 0
    print(count)

part1()
