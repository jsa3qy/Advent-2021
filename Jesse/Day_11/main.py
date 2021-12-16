import copy
from timeit import default_timer as timer

def part_1():
    start_t = timer()
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    flashes = 0
    for _ in range(100):
        changed = False
        lines_copy = copy.deepcopy(lines)
        # increase by 1
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                lines[row][col] += 1
                lines_copy[row][col] += 1
                if lines[row][col] > 9:
                    lines[row][col] = 0
                    lines_copy[row][col] = 0
        # add to those near a flash
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines_copy[row][col] != 0:
                    adjacent_zeros_count = adjacent_zeros(lines, row, col)
                    lines[row][col] += adjacent_zeros_count
                    lines_copy[row][col] += adjacent_zeros_count
                    if lines_copy[row][col] > 9:
                        changed = True      
        # keep looping through and changing cells that need it until we stabalize   
        while changed:
            changed = False
            for row in range(len(lines)):
                for col in range(len(lines[row])):
                    if lines_copy[row][col] > 9:
                        lines_copy[row][col] = 0
                        # use lines to reference, lines_copy is actually changed
                        for cell in get_adj_cells(lines, row, col):
                            if lines_copy[cell[0]][cell[1]] != 0:
                                lines_copy[cell[0]][cell[1]] += 1
                                if lines_copy[cell[0]][cell[1]] > 9:
                                    changed = True
        
        for line in lines_copy:
            flashes += line.count(0)
        lines = lines_copy 

    return flashes, timer() - start_t
        
def part_2():
    start_t = timer()
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    flashes = 0
    step = 0
    while True:
        step += 1
        changed = False
        lines_copy = copy.deepcopy(lines)
        # increase by 1
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                lines[row][col] += 1
                lines_copy[row][col] += 1
                if lines[row][col] > 9:
                    lines[row][col] = 0
                    lines_copy[row][col] = 0
        # add to those near a flash
        for row in range(len(lines)):
            for col in range(len(lines[row])):
                if lines_copy[row][col] != 0:
                    adjacent_zeros_count = adjacent_zeros(lines, row, col)
                    lines[row][col] += adjacent_zeros_count
                    lines_copy[row][col] += adjacent_zeros_count
                    if lines_copy[row][col] > 9:
                        changed = True        
        # keep looping through and changing cells that need it until we stabalize   
        while changed:
            changed = False
            for row in range(len(lines)):
                for col in range(len(lines[row])):
                    if lines_copy[row][col] > 9:
                        lines_copy[row][col] = 0
                        # use lines to reference, lines_copy is actually changed
                        for cell in get_adj_cells(lines, row, col):
                            if lines_copy[cell[0]][cell[1]] != 0:
                                lines_copy[cell[0]][cell[1]] += 1
                                if lines_copy[cell[0]][cell[1]] > 9:
                                    changed = True

        cur_flashes = 0
        for line in lines_copy:
            cur_flashes += line.count(0)

        if cur_flashes == 100:
            return step, timer() - start_t
        flashes += cur_flashes
        lines = lines_copy 
        
    return -1 

def get_adj_cells(lines, row, col):
    cells = []
    if row > 0 and col > 0:
        cells.append((row - 1,col - 1))
    if row > 0:
        cells.append((row - 1,col))
    if col > 0:
        cells.append((row,col - 1))
    if row > 0 and col < len(lines[row]) - 1:
        cells.append((row - 1,col + 1))
    if col < len(lines[row]) - 1:
        cells.append((row,col + 1))
    if row < len(lines) - 1:
        cells.append((row + 1,col))
    if row < len(lines) - 1 and col > 0:
        cells.append((row + 1,col - 1))
    if row < len(lines) - 1 and col < len(lines[row]) - 1:
        cells.append((row + 1,col + 1))
    return cells

def adjacent_zeros(lines, row, col):
    zeros = []
    adj_cells = get_adj_cells(lines, row, col)
    for cell in adj_cells:
        zeros.append(lines[cell[0]][cell[1]])
    return zeros.count(0)

def pretty_print(lines):
    print("\n")
    for line in lines:
        print("".join([str(char) for char in line]))
    print("\n")

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))