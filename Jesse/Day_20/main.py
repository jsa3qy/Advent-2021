from timeit import default_timer as timer
import copy

def part_1(runs = 2):
    start = timer()
    lines = [line.strip() for line in open("input.txt")]
    algo = ""
    image = []
    for index,val in enumerate(lines):
        algo += val
        if val == "":
            image = lines[index + 1:]
            
    for index,line in enumerate(image):
        image[index] = [char for char in line]

    for _ in range(runs + 1):
        image = man_pad(image)
        
    image_copy = copy.deepcopy(image)

    for i in range(runs):
        for y in range(len(image)):
            for x in range(len(image[0])):
                coords = get_nine_coords((x,y))
                build_str = ""
                for coord in coords:
                    if in_bounds(image, coord[0], coord[1]):
                        build_str += image[coord[1]][coord[0]]
                    elif i%2 == 0 and algo[0] == "#":
                        build_str += "."
                    elif i%2 == 1 and algo[0] == "#":
                        build_str += "#"
                    else:
                        build_str += "."
                image_copy[y][x] = algo[int(build_str.replace(".","0").replace("#","1"),2)]
        image = copy.deepcopy(image_copy)

    answer = 0
    for row in image:
        answer += row.count("#")
        
    return answer, timer() - start

def part_2():
    return part_1(50)

def man_pad(image):
    for index,line in enumerate(image):
        image[index] = ["."] + line + ["."]
    return [["."]*len(image[0])] + image + [["."]*len(image[0])]

def get_nine_coords(point):
    x = point[0]
    y = point[1]
    return [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]

def in_bounds(image, x, y):
    return x >= 0 and x < len(image[0]) and y >= 0 and y < len(image)

if __name__ == "__main__":
    part_1_result, time_1 = part_1()
    print("Part 1: " + str(part_1_result) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))