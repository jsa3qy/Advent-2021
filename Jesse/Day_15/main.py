import sys
import copy
from timeit import default_timer as timer

def part_1():
    start = timer()
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    return mutual_helper(lines), timer() - start

def part_2():
    start = timer()
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    for index,line in enumerate(lines):
        line_copy = copy.copy(line)
        for i in range(1,5):
            lines[index] += [val + i if val + i <= 9 else val + i - 9 for val in line_copy]
    lines_copy = copy.deepcopy(lines)
    for i in range(1,5):
        for line in lines_copy:
            lines.append([val + i if val + i <= 9 else val + i - 9 for val in line])
    return mutual_helper(lines), timer() - start

def mutual_helper(lines):
    N = len(lines)
    costs= [[sys.maxint]*N for _ in range(N)]
    costs[0][0] = lines[0][0]
    has_changed = True
    while has_changed:
        has_changed = False
        for y in range(N):
            for x in range(N):
                cur_cells_of_interest = get_neigh_cells(x, y, N)
                min_adj_cost = sys.maxsize
                for adj_cell in cur_cells_of_interest:
                    cur = costs[adj_cell[1]][adj_cell[0]]
                    if cur < min_adj_cost:
                        min_adj_cost = cur
                before_update = costs[y][x]
                after_update = min(min_adj_cost + lines[y][x], before_update)
                costs[y][x] = after_update
                if not has_changed and before_update != after_update:
                    has_changed = True
    return costs[N - 1][N - 1] - costs[0][0]

def get_neigh_cells(x,y,N):
    cells = []
    if x > 0:
        cells.append((x-1,y))
    if y > 0:
        cells.append((x,y-1))
    if x < N - 1:
        cells.append((x + 1, y))
    if y < N - 1:
        cells.append((x, y + 1))
    return cells

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))