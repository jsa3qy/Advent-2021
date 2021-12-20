from timeit import default_timer as timer
import numpy as np
import numpy as np
import copy

def eu_dist(coords_1,coords_2):
    p1 = np.array([coords_1[0], coords_1[1], coords_1[2]])
    p2 = np.array([coords_2[0], coords_2[1], coords_2[2]])
    squared_dist = np.sum((p1-p2)**2, axis=0)
    return np.sqrt(squared_dist)

def all_point_versions(point):
    x = point[0]
    y = point[1]
    z = point[2]
    return [
        [x,y,z],
        [x,-y,-z],
        [-x,y,-z],
        [-x,-y,z],
        [x,z,-y],
        [x,-z,y],
        [-x,z,y],
        [-x,-z,-y],
        [y,x,-z],
        [y,-x,z],
        [-y,x,z],
        [-y,-x,-z],
        [y,z,x],
        [y,-z,-x],
        [-y,z,-x],
        [-y,-z,x],
        [z,x,y],
        [z,-x,-y],
        [-z,x,-y],
        [-z,-x,y],
        [z,y,-x],
        [z,-y,x],
        [-z,y,x],
        [-z,-y,-x]
    ]
    
def get_and_clean_data():
    lines = [line.strip() for line in open("input.txt")]
    filter(lambda val: val !=  "", lines)
    scanner_to_points = {}
    cur_scanner = lines[0]
    for line in lines:
        if "scanner" in line:
            cur_scanner = line
            scanner_to_points[cur_scanner] = []
        elif "," in line:
            scanner_to_points[cur_scanner].append([int(char) for char in line.split(",")])
    return scanner_to_points

def get_distances_to_all_points(scanner_to_points):
    scanner_to_points_map = {}
    for scanner in scanner_to_points.keys():
            s1_points_to_distances = {}
            points = scanner_to_points[scanner]
            for index,point in enumerate(points):
                point_str = "*".join([str(char) for char in point])
                for index2,point2 in enumerate(points):
                    if index != index2:
                        if s1_points_to_distances.get(point_str):
                            s1_points_to_distances[point_str].append(eu_dist(point,point2))
                        else:
                            s1_points_to_distances[point_str] = [eu_dist(point,point2)]
            scanner_to_points_map[scanner] = s1_points_to_distances
    return scanner_to_points_map

def get_shared_points_map(scanner_to_point_to_distances):
    scanners_to_shared_points = {}
    for scanner in scanner_to_point_to_distances.keys():
        for scanner2 in scanner_to_point_to_distances.keys():
            if scanner != scanner2:
                points_map = scanner_to_point_to_distances[scanner]
                points_map_2 = scanner_to_point_to_distances[scanner2]
                for point in points_map.keys():
                    for point2 in points_map_2.keys():
                        intersection = set(points_map[point]).intersection(set(points_map_2[point2]))
                        if len(intersection) > 10:
                            point_str = [int(char) for char in point.split("*")]
                            point2_str = [int(char) for char in point2.split("*")]
                            cleaned_scanner_names = scanner.strip(" -scanner") + "-" + scanner2.strip(" -scanner")
                            if scanners_to_shared_points.get(cleaned_scanner_names):
                                scanners_to_shared_points[cleaned_scanner_names].append([point_str,point2_str])
                            else:
                                scanners_to_shared_points[cleaned_scanner_names] = [[point_str,point2_str]]
    return scanners_to_shared_points

def order_keys(cur_keys):
    next_keys = []
    cur_key = "0"
    seen = []
    cleaned_keys = []
    while True:
        seen.append(cur_key)
        for key in cur_keys:
            if key.split("-")[0] == cur_key:
                if key not in cleaned_keys:
                    cleaned_keys.append(key)
                if key.split("-")[1] not in seen:
                    next_keys.append(key.split("-")[1])
        if len(next_keys) == 0:
            break
        cur_key = next_keys.pop()
    return cleaned_keys

def manhat(point1,point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2])

def apply_translation(point, translation):
    point_0 = point[0]
    point_1 = point[1]
    point_2 = point[2]
    return [point_0 + translation[0], point_1 + translation[1], point_2 + translation[2]]

def get_translation(points_0, points_1):
    orientations = all_point_versions(points_1[0])
    target = points_0[0]
    for or_index,orientation in enumerate(orientations):
        translation = [target[0] - orientation[0], target[1] - orientation[1], target[2] - orientation[2]]
        success_counter = 0
        for index2 in range(1,len(points_0)):
            point_attempt = copy.copy(points_1[index2])
            point_attempt = apply_translation(all_point_versions(point_attempt)[or_index],translation)
            if point_attempt == points_0[index2]:
                success_counter += 1
        if success_counter == 11:
            return translation, or_index
    return None, None

def part_1():
    start = timer()
    scanner_to_points = get_and_clean_data()
    scanner_to_point_to_distances = get_distances_to_all_points(scanner_to_points)
    scanners_to_shared_points = get_shared_points_map(scanner_to_point_to_distances)

    cur_keys = sorted(scanners_to_shared_points.keys())
    cur_keys = sorted(cur_keys, key=lambda x: (int(x.split("-")[0]),int(x.split("-")[1])))
    cleaned_keys = order_keys(cur_keys)
    helped_scanners = ["0"]
    points = scanner_to_points["--- scanner 0 ---"]
    key_to_translation = {}
    for key in cleaned_keys:
        scanner_2_id = key.split("-")[1] 
        if scanner_2_id not in helped_scanners:
            helped_scanners.append(scanner_2_id)
            next_num = scanner_2_id
            cur_points = scanners_to_shared_points[key]
            points_0 = [val[0] for val in cur_points]
            points_1 = [val[1] for val in cur_points]
            translation, or_index = get_translation(points_0, points_1)
            key_to_translation[next_num] = translation
            for point in scanner_to_points["--- scanner " + next_num + " ---"]:
                new_point = apply_translation(all_point_versions(copy.copy(point))[or_index], translation)                        
                if new_point not in points:
                    points.append(new_point)
            seen = []
            for key2 in cleaned_keys:
                if key2.split("-")[0] == next_num and key2.split("-")[1] not in helped_scanners and key2 not in seen:
                    seen.append(key2)
                    for index,_ in enumerate(scanners_to_shared_points[key2]):
                        scanners_to_shared_points[key2][index][0] = apply_translation(all_point_versions(scanners_to_shared_points[key2][index][0])[or_index], translation)
    points = sorted(points, key=lambda x: x[0])
    return key_to_translation,len(points), timer() - start

def part_2(key_to_translation = None):
    start = timer()
    if not key_to_translation:
        key_to_translation, _, _ = part_1()
    translations = key_to_translation.values()
    max_val = 0
    for index,translation in enumerate(translations):
        for index2,translation2 in enumerate(translations):
            if index != index2:
                max_val = max(max_val,manhat(translation, translation2))
    return max_val, timer() - start

if __name__ == "__main__":
    key_to_translation, part_1_res, time_1 = part_1()
    print("Part 1: " + str(part_1_res) + " in " + str(time_1))
    part_2, time_2 = part_2(key_to_translation)
    print("Part 2: " + str(part_2) + " in " + str(time_2))