def part_1():
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    lows = []
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            cur_height = lines[row][col]
            if row > 0:
                if not lines[row - 1][col] > cur_height:
                    continue
            if row < len(lines) - 1:
                if not lines[row + 1][col] > cur_height:
                    continue
            if col > 0:
                if not lines[row][col - 1] > cur_height:
                    continue
            if col < len(lines[0]) - 1:
                if not lines[row][col + 1] > cur_height:
                    continue
            lows.append(cur_height)
    return sum(lows) + len(lows)

def part_2():
    lines = [[int(char) for char in line.strip()] for line in open("input.txt")]
    seen_matrix = [[0]*len(lines[0]) for i in range(len(lines))]
    basin_counts = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            basin_counts.append(get_basin_count(row,col,lines,seen_matrix))
    basin_counts = sorted(basin_counts)
    return basin_counts[len(basin_counts) - 1]*basin_counts[len(basin_counts) - 2]*basin_counts[len(basin_counts) - 3]

def get_basin_count(row, col, matrix, seen_matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return 0
    elif seen_matrix[row][col] == 1 or matrix[row][col] == 9:
        return 0
    else:
        seen_matrix[row][col] = 1
        return_val = 1
        return_val += get_basin_count(row + 1, col, matrix, seen_matrix)
        return_val += get_basin_count(row - 1, col, matrix, seen_matrix)
        return_val += get_basin_count(row, col - 1, matrix, seen_matrix)
        return_val += get_basin_count(row, col + 1, matrix, seen_matrix)
        return return_val

if __name__ == "__main__":
    print("Part 1: " + str(part_1()))
    print("Part 2: " + str(part_2()))