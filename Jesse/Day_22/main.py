import enum
from timeit import default_timer as timer
import re
import sys
import copy

def part_1():
    start = timer()
    lines = [line.strip() for line in open("input.txt")]
    seen = {}
    for line in lines:
        split = line.split(" ")
        on_off = split[0]
        coords = [[int(val) for val in char.split("..")] for char in re.findall("[-]*[0-9]+..[-]*[0-9]+", split[1])]
        x_range = coords[0]
        y_range = coords[1]
        z_range = coords[2]
        if x_range[0] > 50 or y_range[0] > 50 or z_range[0] > 50 or x_range[1] < -50 or y_range[1] < -50 or z_range[1] < -50:
            continue
        
        if x_range[0] < -50:
            x_range[0] = -50
        if x_range[1] > 50:
            x_range[1] = 50
        if y_range[0] < -50:
            y_range[0] = -50
        if y_range[1] > 50:
            y_range[1] = 50
        if z_range[0] < -50:
            z_range[0] = -50
        if z_range[1] > 50:
            z_range[1] = 50
        for x in range(x_range[0],x_range[1] + 1):
            for y in range(y_range[0],y_range[1] + 1):
                for z in range(z_range[0],z_range[1] + 1):
                    if (on_off == "on"):
                        seen["-".join([str(x), str(y), str(z)])] = 1
                    else:
                        seen["-".join([str(x), str(y), str(z)])] = 0
                     
    return seen.values().count(1), timer() - start

def part_2():
    start = timer()
    lines = [line.strip() for line in open("input.txt")]
    working_list = []

    for index,line in enumerate(lines):
        split = line.split(" ")
        on_off = split[0]
        coords = [[int(val) for val in char.split("..")] for char in re.findall("[-]*[0-9]+..[-]*[0-9]+", split[1])]
        new_working_list = copy.deepcopy(working_list)
        if on_off == "on":
            for val in working_list:
                if val[0] == "+":
                    inter = get_matrix_intersection(val[1],coords)
                    if inter.count(0) == 0:
                        new_working_list.append(["-",inter])
                elif val[0] == "-":
                    inter = get_matrix_intersection(val[1],coords)
                    if inter.count(0) == 0:
                        new_working_list.append(["+", inter])
            new_working_list.append(["+",coords])
        elif on_off == "off":
            for val in working_list:
                if val[0] == "+":
                    inter = get_matrix_intersection(val[1],coords)
                    if inter.count(0) == 0:
                        new_working_list.append(["-",inter])
                elif val[0] == "-":
                    inter = get_matrix_intersection(val[1],coords)
                    if inter.count(0) == 0:
                        new_working_list.append(["+",inter])
        working_list = copy.deepcopy(new_working_list)
    
    count = 0
    for val in working_list:
        plus_or_minus = val[0]
        ranges = val[1]
        if plus_or_minus == "+":
            count += ((ranges[0][1] - ranges[0][0] + 1) * (ranges[1][1] - ranges[1][0] + 1) * (ranges[2][1] - ranges[2][0] + 1))
        if plus_or_minus == "-":
            count -= ((ranges[0][1] - ranges[0][0] + 1) * (ranges[1][1] - ranges[1][0] + 1) * (ranges[2][1] - ranges[2][0] + 1))
        
    return count, timer() - start

def get_matrix_intersection(coords1, coords2):
    x_range_1 = coords1[0]
    y_range_1 = coords1[1]
    z_range_1 = coords1[2]
    x_range_2 = coords2[0]
    y_range_2 = coords2[1]
    z_range_2 = coords2[2]
    x_overlap = 0
    y_overlap = 0
    z_overlap = 0
    if overlap(x_range_1, x_range_2):
        x_overlap = [max(x_range_1[0], x_range_2[0]), min(x_range_1[1], x_range_2[1])]
    if overlap(y_range_1, y_range_2):
        y_overlap = [max(y_range_1[0], y_range_2[0]), min(y_range_1[1], y_range_2[1])]
    if overlap(z_range_1, z_range_2):
        z_overlap = [max(z_range_1[0], z_range_2[0]), min(z_range_1[1], z_range_2[1])]
    return [
        x_overlap,
        y_overlap,
        z_overlap
        ]

def overlap(range1, range2):
    return not (range1[0] > range2[1] or range2[0] > range1[1])

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))