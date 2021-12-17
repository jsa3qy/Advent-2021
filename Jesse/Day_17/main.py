from timeit import default_timer as timer

def within_target(x,y,target_range):
    return x <= target_range[0][1] and x >= target_range[0][0] and y <= target_range[1][1] and y >= target_range[1][0]

def beyond_target(x,y,target_range):
    return x > target_range[0][1] or y < target_range[1][0]

def calc_new_pos(x,y,x_v,y_v):
    x += x_v
    y += y_v
    if x_v < 0:
        x_v += 1
    elif x_v > 0:
        x_v -= 1
    y_v -= 1
    return x,y,x_v,y_v

def get_max_y(y_v):
    y = 0
    old_y = -1
    while old_y < y:
        old_y = y
        y += y_v
        y_v -= 1
    return old_y

def part_1():
    start = timer()
    input = "target area: x=138..184, y=-125..-71"
    ranges = input.strip().split(" ")[2:]
    for index,val in enumerate(ranges):
        ranges[index] = [int(el) for el in val.strip("xy=,").split("..")]
        
    cur_x = 0
    cur_y = 0
    
    sol_not_found = True
    
    start_x_v = 0
    start_y_v = 0
    
    max_x_v = ranges[0][1]
    min_y_v = ranges[1][0]
    
    answers = []
    
    while sol_not_found:
        x_v = start_x_v + 1
        start_x_v = x_v
        if x_v > max_x_v:
            break
        still_possible_for_x_v = True
        while still_possible_for_x_v:
            still_possible_for_y_v = True
            y_v = 0
            start_y_v = min_y_v
            while still_possible_for_y_v:
                cur_x,cur_y,x_v,y_v = calc_new_pos(cur_x,cur_y,x_v,y_v)
                if within_target(cur_x,cur_y,ranges):
                    answers.append((start_x_v, start_y_v))
                if beyond_target(cur_x,cur_y,ranges):
                    cur_x = 0
                    cur_y = 0
                    y_v = start_y_v + 1
                    start_y_v = y_v
                    if y_v > 200:
                        still_possible_for_y_v = False
                        still_possible_for_x_v = False
                    x_v = start_x_v

    answers.sort(key = lambda x: x[1])
    
    max = answers[0]
    for answer in answers:
        max_y = get_max_y(answer[1])
        if max_y > get_max_y(max[1]):
            max = answer
        
    return max[1],get_max_y(max[1]), timer() - start

def part_2(y_v_bound = 200):
    start = timer()
    input = "target area: x=138..184, y=-125..-71"
    ranges = input.strip().split(" ")[2:]
    for index,val in enumerate(ranges):
        ranges[index] = [int(el) for el in val.strip("xy=,").split("..")]
        
    cur_x = 0
    cur_y = 0
    
    sol_not_found = True
    
    start_x_v = 0
    
    max_x_v = ranges[0][1]
    min_y_v = ranges[1][0]
    
    answers = []
    
    while sol_not_found:
        start_x_v += 1
        x_v = start_x_v
        if x_v > max_x_v:
            break
        still_possible_for_x_v = True
        while still_possible_for_x_v:
            still_possible_for_y_v = True
            y_v = min_y_v
            start_y_v = min_y_v
            while still_possible_for_y_v:
                cur_x,cur_y,x_v,y_v = calc_new_pos(cur_x,cur_y,x_v,y_v)
                if within_target(cur_x,cur_y,ranges):
                    answers.append((start_x_v, start_y_v))
                if beyond_target(cur_x,cur_y,ranges):
                    cur_x = 0
                    cur_y = 0
                    y_v = start_y_v + 1
                    start_y_v = y_v
                    if y_v > y_v_bound:
                        still_possible_for_y_v = False
                        still_possible_for_x_v = False
                    x_v = start_x_v
        
    return len(list(set(answers))), timer() - start

if __name__ == "__main__":
    y_v_bound,part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2(y_v_bound)
    print("Part 2: " + str(part_2) + " in " + str(time_2))