def part_1():
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
    
    return depth*hor_pos

def part_2():
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
    
    return depth*hor_pos

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))