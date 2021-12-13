def part_1():
    dots = [[int(val) for val in line.strip().split(",")] for line in open("input.txt")]
    ints = [line.strip().split(" ")[-1].split("=") for line in open("instructions.txt")]
    seen = {}
    for dot in dots:
        seen[str(dot[0]) + "," + str(dot[1])] = 1
        
    intstruction = ints[0]
    if intstruction[0] == "x":
        for dot in dots:
            new_dot = flip_left(dot, int(intstruction[1]))
            if dot != new_dot:
                seen.pop(dot_to_string(dot))
                seen[dot_to_string(new_dot)] = 1
    elif intstruction[0] == "y":
        for dot in dots:
            new_dot = flip_up(dot, int(intstruction[1]))
            if dot != new_dot:
                seen.pop(dot_to_string(dot))
                seen[dot_to_string(new_dot)] = 1

    return len(seen)

def part_2():
    dots = [[int(val) for val in line.strip().split(",")] for line in open("input.txt")]
    ints = [line.strip().split(" ")[-1].split("=") for line in open("instructions.txt")]
    seen = {}
    for dot in dots:
        seen[str(dot[0]) + "," + str(dot[1])] = 1
        
    for instruction in ints:
        if instruction[0] == "x":
            for dot in dots:
                new_dot = flip_left(dot, int(instruction[1]))
                if dot != new_dot:
                    seen.pop(dot_to_string(dot))
                    seen[dot_to_string(new_dot)] = 1
        elif instruction[0] == "y":
            for dot in dots:
                new_dot = flip_up(dot, int(instruction[1]))
                if dot != new_dot:
                    seen.pop(dot_to_string(dot))
                    seen[dot_to_string(new_dot)] = 1
        dots = [[int(val) for val in line.split(",")] for line in seen.keys()]

    return build_return_val(dots)

def dot_to_string(dot):
    return str(dot[0]) + "," + str(dot[1])

def flip_up(point, y):
    val = point[1]
    if val > y:
        num_above_y = y - (val - y)
        return (point[0],num_above_y)
    return point

def flip_left(point, x):
    val = point[0]
    if val > x:  
        num_left_x = x - (val - x)
        return (num_left_x,point[1])
    return point

def build_return_val(dots):
    q_map = {}
    for val in dots:
        if q_map.get(val[1]):
            q_map[val[1]].append(val[0])
        else:
            q_map[val[1]] = [val[0]]
    cur_str = "\n\n"   
    for val in sorted(q_map.keys()):
        for x in range(max(q_map[val]) + 1):
            if x in q_map[val]:
                cur_str += "X"
            else:
                cur_str += " "
        cur_str += "\n"
    return cur_str

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))