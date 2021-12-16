import scipy.special
from timeit import default_timer as timer

def part_1():
    start_t = timer()
    lines = [int(val) for val in open("input.txt").readline().strip().split(",")]
    tracker = [0]*max(lines)
    for val in lines:
        for ind,_ in enumerate(tracker):
            tracker[ind] += abs(val - ind)
    return min(tracker), timer() - start_t

def part_2():
    start_t = timer()
    lines = [int(val) for val in open("input.txt").readline().strip().split(",")]
    tracker = [0]*max(lines)
    for val in lines:
        for ind,_ in enumerate(tracker):
            tracker[ind] += binominal_co(abs(val - ind))
    return min(tracker), timer() - start_t

def binominal_co(val):
    return int(scipy.special.binom(val + 1, 2))

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))