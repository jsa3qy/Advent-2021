import scipy.special

def part_1():
    lines = [int(val) for val in open("input.txt").readline().strip().split(",")]
    tracker = [0]*max(lines)
    for val in lines:
        for ind,_ in enumerate(tracker):
            tracker[ind] += abs(val - ind)
    return min(tracker)

def part_2():
    lines = [int(val) for val in open("input.txt").readline().strip().split(",")]
    tracker = [0]*max(lines)
    for val in lines:
        for ind,_ in enumerate(tracker):
            tracker[ind] += binominal_co(abs(val - ind))
    return min(tracker)

def binominal_co(val):
    return int(scipy.special.binom(val + 1, 2))

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))