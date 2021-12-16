from timeit import default_timer as timer

def part_1():
    start_t = timer()
    lines = [int(line.strip()) for line in open("input.txt")]
    increased = 0
    for index,val in enumerate(lines):
        if index > 0:
            if val > lines[index - 1]:
                increased += 1
    return increased, timer() - start_t

def part_2():
    start_t = timer()
    lines = [int(line.strip()) for line in open("input.txt")]
    increased = 0
    for index,val in enumerate(lines):
        if index < len(lines) - 3:
            if val + lines[index + 1] + lines[index + 2]  < lines[index + 1] + lines[index + 2] + lines[index + 3]:
                increased += 1
    return increased, timer() - start_t

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))