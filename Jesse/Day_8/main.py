mapping = {
    2 : 1,
    4 : 4,
    3 : 7,
    7 : 8
}

known = [1,4,7,8]
not_known = [0, 2, 3, 5, 6, 9]

all = ["a","b","c","d","e","f","g"]

def part_1():
    lines = [[val.strip().split(" ") for val in line.strip().split("|")] for line in open("input.txt")]
    count = 0
    for line in lines:
        for val in line[1]:
            if mapping.get(len(val)):
                count += 1
    return count

#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

#  0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def part_2():
    num_to_used_indices = {
        0 : [0,1,2,4,5,6],
        1 : [2,5],
        2 : [0,2,3,4,6],
        3 : [0,2,3,5,6],
        4 : [1,2,3,5],
        5 : [0,1,3,5,6],
        6 : [0,1,3,4,5,6],
        7 : [0,2,5],
        8 : [0,1,2,3,4,5,6],
        9 : [0,1,2,3,5,6]
    }
    
    numletters_to_numbers = {
        0 : [],
        1 : [],
        2 : [1],
        3 : [7],
        4 : [4],
        5 : [2,3,5],
        6 : [0,6,9],
        7 : [8]
    }
    
    decoder = {
        "0-1-2-4-5-6" : 0,
        "2-5" : 1,
        "0-2-3-4-6" : 2,
        "0-2-3-5-6" : 3,
        "1-2-3-5" : 4,
        "0-1-3-5-6" : 5,
        "0-1-3-4-5-6" : 6,
        "0-2-5" : 7,
        "0-1-2-3-4-5-6" : 8,
        "0-1-2-3-5-6" : 9
    }

    answer = 0
    lines = [[val.strip().split(" ") for val in line.strip().split("|")] for line in open("input.txt")]
    for line in lines:
        num_to_coded = {}
        unknown = []
        for val in line[0] + line[1]:
            # sort for consistency
            val = "".join(sorted(val))
            if mapping.get(len(val)):
                num_to_coded[mapping.get(len(val))] = [char for char in val]
            else:
                if val not in unknown:
                    unknown.append(val)
    
        for val in not_known:
            num_to_coded[val] = ["a","b","c","d","e","f","g"]
        
        index_to_possible = {}
        for i in range(7):
            index_to_possible[i] = ["a","b","c","d","e","f","g"]

        # For each known value, take the indices it uses, 
        # and define possible chars as the chars in the strings we know belong to the known
        for known_val in known:
            for num in num_to_used_indices[known_val]:
                # intersection might not actually be needed here, probs can just set it to num_to_coded[known_val]
                index_to_possible[num] = get_intersection_k([num_to_coded[known_val], index_to_possible[num]])
        
        # for each known value, we know the indices it uses, 
        # remove the known values chars from all other indices 
        for known_val in known:
            for index in range(7):
                if index not in num_to_used_indices[known_val]:
                    for char in num_to_coded[known_val]:
                        if char in index_to_possible[index]:
                            index_to_possible[index].remove(char)
                            
        # # use number of letters to determine final cleaning
        sixes = []
        fives = []
        for unknown_val in unknown:
            if len(unknown_val) == 6:
                sixes += [char for char in unknown_val]
            if len(unknown_val) == 5:
                fives += [char for char in unknown_val]

        # collect the common letters across the 3 len() == 5 and 3 len() == 6
        new_sixes = []
        for val in sixes:
            if sixes.count(val) == 3:
                new_sixes.append(val)
        new_fives = []
        for val in set(fives):
            if fives.count(val) == 3:
                new_fives.append(val)

        fives = new_fives
        sixes = new_sixes
        sixes = list(set(sixes))
        fives = list(set(fives))
        
        # get the indices that these shared segments across the fivers and sixers correspond to
        shared_sixer_indices = []
        for sixer in numletters_to_numbers[6]:
            if len(shared_sixer_indices) == 0:
                shared_sixer_indices = num_to_used_indices[sixer]
            else:    
                shared_sixer_indices = get_intersection_k([shared_sixer_indices, num_to_used_indices[sixer]])

        for index in shared_sixer_indices:
            index_to_possible[index] = get_intersection_k([sixes,index_to_possible[index]])
            
        for index,key in enumerate(index_to_possible.keys()):
            if len(index_to_possible[key]) == 1:
                for index2,key2 in enumerate(index_to_possible.keys()):
                    if index != index2:
                        if index_to_possible[key][0] in index_to_possible[key2]:
                            index_to_possible[key2].remove(index_to_possible[key][0])
                            

        shared_fiver_indices = []
        for fiver in numletters_to_numbers[5]:
            if len(shared_fiver_indices) == 0:
                shared_fiver_indices = num_to_used_indices[fiver]
            else:    
                shared_fiver_indices = get_intersection_k([shared_fiver_indices, num_to_used_indices[fiver]])

        for index in shared_fiver_indices:
            index_to_possible[index] = get_intersection_k([fives,index_to_possible[index]])
            
        for index,key in enumerate(index_to_possible.keys()):
            if len(index_to_possible[key]) == 1:
                for index2,key2 in enumerate(index_to_possible.keys()):
                    if index != index2:
                        if index_to_possible[key][0] in index_to_possible[key2]:
                            index_to_possible[key2].remove(index_to_possible[key][0])
        
        for key in index_to_possible:
            val = index_to_possible[key]
            if len(val) > 1:
                index_to_possible[key] = [val[0]]

        letter_to_num = {v[0]: str(k) for k, v in index_to_possible.items()}
        
        line_val = ""
        for piece in line[1]:
            new_string = []
            piece = [char for char in piece]
            for char in "".join(piece):
                new_string.append(letter_to_num[char])
                new_string = sorted(new_string)
            line_val += str(decoder["-".join(new_string)])

        answer += int(line_val)
    return answer

def get_intersection_k(list_of_lists):
    return list(set.intersection(*map(set,list_of_lists)))
    
if __name__ == "__main__":
    print("Part 1: " + str(part_1()))
    print("Part 2: " + str(part_2()))