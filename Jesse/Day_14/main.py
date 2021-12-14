def part_1():
    start = [line.strip() for line in open("starter.txt")][0]
    rules = [[rule.strip() for rule in line.strip().split("->")] for line in open("input.txt")]
    rule_map = {}
    for rule in rules:
        rule_map[rule[0]] = rule[1]

    for _ in range(10):
        new_str = start[0]
        for index in range(len(start) - 1):
            rule_val = rule_map.get(start[index:index+2])
            if rule_val:
                new_str += rule_val + start[index + 1]
            else:
                new_str += start[index+1:index+2]
        start = new_str
            
    uniques = list(set([char for char in start]))
    chars = [char for char in start]
    max = 0
    min = len(start)
    for unique in uniques:
        if chars.count(unique) > max:
            max = chars.count(unique)
        if chars.count(unique) < min:
            min = chars.count(unique)
            
    return max - min

def part_2():
    start = [line.strip() for line in open("starter.txt")][0]
    rules = [[rule.strip() for rule in line.strip().split("->")] for line in open("input.txt")]

    rule_map = {}
    for rule in rules:
        rule_map[rule[0]] = rule[1]
        
    pair_counts = {}
    letter_counts = {}
    letter_counts[start[len(start) - 1]] = 1
    for index in range(len(start) - 1):
        if letter_counts.get(start[index]):
            letter_counts[start[index]] += 1
        else:
            letter_counts[start[index]] = 1
        if pair_counts.get(start[index:index+2]):
            pair_counts[start[index:index+2]] += 1
        else:
            pair_counts[start[index:index+2]] = 1

    for i in range(40):
        pair_counts_new = {}
        for val in pair_counts:
            insert_val = rule_map.get(val)
            if insert_val:
                if pair_counts.get(val):
                    if letter_counts.get(insert_val):
                        letter_counts[insert_val] += pair_counts[val]
                    else:
                        letter_counts[insert_val] = pair_counts[val]
                    if pair_counts_new.get(val[0] + insert_val):
                        pair_counts_new[val[0] + insert_val] += pair_counts[val]
                    else:
                        pair_counts_new[val[0] + insert_val] = pair_counts[val]
                    if pair_counts_new.get(insert_val + val[1]):
                        pair_counts_new[insert_val + val[1]] += pair_counts[val]
                    else:
                        pair_counts_new[insert_val + val[1]] = pair_counts[val]
        pair_counts = pair_counts_new

    inv_map = {int(v): k for k, v in letter_counts.items()}
    min_v = min(inv_map.keys())
    max_v = max(inv_map.keys())
    
    return max_v - min_v

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))