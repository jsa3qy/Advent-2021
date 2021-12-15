def part_1():
    lines = [int(line.strip()) for line in open("input.txt")]
    increased = 0
    for index,val in enumerate(lines):
        if index > 0:
            if val > lines[index - 1]:
                increased += 1
    return increased

def part_2():
    lines = [int(line.strip()) for line in open("input.txt")]
    increased = 0
    for index,val in enumerate(lines):
        if index < len(lines) - 3:
            if val + lines[index + 1] + lines[index + 2]  < lines[index + 1] + lines[index + 2] + lines[index + 3]:
                increased += 1
    return increased

if __name__ == "__main__":
    print("Part 1: " + str(part_1()))
    print("Part 2: " + str(part_2()))