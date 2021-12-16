from timeit import default_timer as timer

def part_1():
    start_t = timer()
    graph = [[0]*1000 for i in range(1000)]
    lines = [line.strip() for line in open("input.txt")]
    input_lines = []
    for line in lines:
        input_line = [val.split(",") for val in line.split(" -> ")]
        if input_line[0][0] == input_line[1][0] or input_line[0][1] == input_line[1][1]:
            input_lines.append(line.split(" -> "))
    count = 0
    for line in input_lines:
        points = points_between(line[0].split(",")[0],line[0].split(",")[1],line[1].split(",")[0],line[1].split(",")[1])
        for point in points:
            if graph[point[1]][point[0]] > 0:
                if graph[point[1]][point[0]] == 1:
                    count += 1
            graph[point[1]][point[0]] += 1

    return count, timer() - start_t

def part_2():
    start_t = timer()
    graph = [[0]*1000 for i in range(1000)]
    input_lines = [line.strip().split(" -> ") for line in open("input.txt")]
    count = 0
    for line in input_lines:
        points = points_between(line[0].split(",")[0],line[0].split(",")[1],line[1].split(",")[0],line[1].split(",")[1]) 
        for point in points:
            if graph[point[1]][point[0]] > 0:
                if graph[point[1]][point[0]] == 1:
                    count += 1
            graph[point[1]][point[0]] += 1
        
    return count, timer() - start_t

def points_between(x1, y1, x2, y2):
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    points = [(x1,y1),(x2,y2)]
    if x1 != x2 and y1 == y2:
        for i in range(min(x1,x2) + 1, max(x1,x2)):
            points.append((i,y1))
    elif y1 != y2 and x1 == x2:
        for i in range(min(y1,y2) + 1, max(y1,y2)):
            points.append((x1,i))
    else:
        if x1 < x2:
            for x in range(x1 + 1, x2):
                if y1 < y2:
                    points.append((x,y1 + (x - x1)))
                else:
                    points.append((x,y1 - (x - x1)))
        else:
            for x in range(x2 + 1, x1):
                if y1 < y2:
                    points.append((x,y2 - (x - x2)))
                else:
                    points.append((x,y2 + (x - x2)))
    return points

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))