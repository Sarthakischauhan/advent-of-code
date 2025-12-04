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

def part2():
    with open("puzzle2.txt", "r") as file:
        reports = file.readlines()
    file.close()

    count = 0

    for report in reports:
        report = report.strip().split(" ")
        report = list(map(int, report))

        prev = report[0]
        inc = None  
        safe = True
        crs = 0
        for i, level in enumerate(report[1:], start=1):
            diff = level - prev

            if 1 <= abs(diff) <= 3:  
                if diff > 0:  
                    if inc is None:  
                        inc = True
                    elif not inc:  
                        if crs < 1:
                            crs += 1
                        else:
                            safe = False
                            break
                elif diff < 0:  
                    if inc is None:
                        inc = False
                    elif inc:  
                        if crs < 1:
                            crs += 1
                        else:
                            safe = False
                            break
            else:  
                if crs < 1:  
                    crs += 1
                else:
                    safe = False
                    break

            prev = level

        count += 1 if safe else 0

    print(count)
part2()
