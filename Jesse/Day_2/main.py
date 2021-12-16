from timeit import default_timer as timer

def part_1():
    start_t = timer()
    depth = 0
    hor_pos = 0
    lines = [line.strip().split(" ") for line in open("input.txt")]
    for ins in lines:
        if ins[0] == "down":
            depth += int(ins[1])
        elif ins[0] == "up":
            depth -= int(ins[1])
        else:
            hor_pos += int(ins[1])
    
    return depth*hor_pos, timer() - start_t

def part_2():
    start_t = timer()
    aim = 0
    depth = 0
    hor_pos = 0
    lines = [line.strip().split(" ") for line in open("input.txt")]
    for ins in lines:
        if ins[0] == "down":
            aim += int(ins[1])
        elif ins[0] == "up":
            aim -= int(ins[1])
        else:
            hor_pos += int(ins[1])
            depth += aim*int(ins[1])
    
    return depth*hor_pos, timer() - start_t

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))