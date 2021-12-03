import copy

def part_1():
    array = [0]*12
    lines = [line.strip() for line in open("input.txt")]
    for val in lines:
        for index,bit in enumerate([char for char in val]):
            if bit == "1":
                array[index] += 1
            else:
                array[index] -= 1
            
    gamma = ""
    epsilon = ""
    for val in array:
        if val < 0:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
            
    return int(gamma, 2)*int(epsilon, 2)

def part_2():
    lines = [line.strip() for line in open("input.txt")]
    lines_copy = copy.deepcopy(lines)
    cur_pos = 0
    while len(lines) > 1:
        is_one_most_common = most_common_is_one_for_position(lines, cur_pos)
        new_lines = get_only_needed_vals(lines, is_one_most_common, cur_pos)
        lines = new_lines
        cur_pos += 1
        
    cur_pos = 0
    while len(lines_copy) > 1:
        is_one_most_common = least_common_is_one_for_position(lines_copy, cur_pos)
        new_lines = get_only_needed_vals(lines_copy, is_one_most_common, cur_pos)
        lines_copy = new_lines
        cur_pos += 1
        
    ox = lines[0]
    co = lines_copy[0]
    return int(ox, 2)*int(co, 2)

def most_common_is_one_for_position(vals, position):
    return_val = 0
    for val in vals:
        if val[position] == "1":
            return_val += 1
        else: 
            return_val -= 1
    if return_val >= 0:
        return "1"
    else:
        return "0"
    
def least_common_is_one_for_position(vals, position):
    return_val = 0
    for val in vals:
        if val[position] == "1":
            return_val += 1
        else: 
            return_val -= 1
    if return_val >= 0:
        return "0"
    else:
        return "1"

def get_only_needed_vals(vals, target, position):
    new_list = []
    for val in vals:
        if val[position] == target:
            new_list.append(val)
    return new_list

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))

# def part_1():
#     lines = [line.strip() for line in open("input.txt")]
#     return

# def part_2():
#     lines = [line.strip() for line in open("input.txt")]
#     return

# print("Part 1: " + str(part_1()))
# print("Part 2: " + str(part_2()))