# Advent of Code 2020
# day1

def loadFile():
    with open('day1input.txt', 'r') as f:
        #print("load file")
        values = []
        for line in f:
            values.append(int(line))
            values.sort()
    return values

def findTwo(values):
    for val in values:
        val2 = 2020 - val
        if (binarySearch(values, val2)):
            return("value 1: " + str(val) +  "\nvalue 2: " + str(val2))

def findThree(values):
    for i, val in enumerate(values):
        for val2 in values[i:]:
            val3 = 2020 - val2 - val
            if (binarySearch(values, val3)):
                return("value 1: " + str(val) +  "\nvalue 2: " + str(val2) + "\nvalue 3: " + str(val3))


#binary search
def binarySearch(values, val2):
    result = False
    l = 0
    r = len(values) - 1
    while l <= r:
        mid = int((r + l) / 2)
        n = values[mid]
        if n == val2:
            return True
        if n > val2:
            r = mid - 1
        else:
            l = mid + 1
    return False


values = loadFile()
print("Day 1 part 1")
print(findTwo(values))
print("Day 1 part 2")
print(findThree(values))

