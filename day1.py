#! usr/bin/python3

# Reading the file through and printing all the lines

def part1():
    with open("puzzle1.txt", "r") as file:
        content = file.readlines()
        
        # Replace all the newline character with an empty space
        content = [line.replace("\n","") for line in content]
        
        left, right = [], []
        
        # Create a list of left and right elements
        for line in content:
            l, r = line.split("   ")
            left.append(int(l))
            right.append(int(r))
        
        # Sort the two list
        left.sort()
        right.sort()
        
        # Start by subtracting sorted_left and sorted_right elements
        final_sum = sum([abs(left[i] - right[i]) for i in range(len(left))])

        print(final_sum)


def part2():
    with open("puzzle1.txt", "r") as file:
        content = file.readlines()
        
        # Replace all the newline character with an empty space
        content = [line.replace("\n","") for line in content]
        
        left, right = [], []
        
        # Create a list of left and right elements
        for line in content:
            l, r = line.split("   ")
            left.append(int(l))
            right.append(int(r))
        
        similarity = 0
        # No need to sort this time
        for l in left:
            count = right.count(l)
            similarity += l * count

        print(similarity)

