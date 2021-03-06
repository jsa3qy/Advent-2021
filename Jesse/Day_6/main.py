import copy
from timeit import default_timer as timer

def part_1():
    start_t = timer()
    line = open("input.txt").readline()
    line = [int(val) for val in line.split(",")]
    for i in range(80):
        new_list = []
        for val in line:
            if val == 0:
                new_list += [6,8]
            else:
                new_list.append(val - 1)
        line = new_list
    return len(line), timer() - start_t

def part_2():
    start_t = timer()
    line = open("input.txt").readline()
    line = [int(val) for val in line.split(",")]
    tracker = [0]*9
    for val in line:
        tracker[val] += 1
    for i in range(256):
        new_tracker = [0]*9
        new_tracker[6] += (tracker[0] + tracker[7])
        new_tracker[8] += tracker[0]
        new_tracker[0] += tracker[1]
        new_tracker[1] += tracker[2]
        new_tracker[2] += tracker[3]
        new_tracker[3] += tracker[4]
        new_tracker[4] += tracker[5]
        new_tracker[5] += tracker[6]
        new_tracker[7] += tracker[8]
        tracker = copy.copy(new_tracker)
    return sum(tracker), timer() - start_t

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))