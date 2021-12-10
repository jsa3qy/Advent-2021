lefts = {
    "{" : "}",
    "[" : "]",
    "<" : ">",
    "(" : ")"
}

def part_1():
    points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
    }
    lines = [line.strip() for line in open("input.txt")]
    answer = 0
    for line in lines:
        stack = []
        for char in line:
            if lefts.get(char):
                stack.append(char)
            else:
                match = stack.pop()
                if char != lefts.get(match):
                    answer += points.get(char)
    return answer

def part_2():
    points = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    scores = []
    lines = [line.strip() for line in open("input.txt")]
    for line in lines:
        stack = []
        ignore = False
        for char in line:
            if lefts.get(char):
                stack.append(char)
            else:
                match = stack.pop()
                if char != lefts.get(match):
                    ignore = True
        if not ignore:
            stack.reverse()
            score = 0
            for val in stack:
                score *= 5
                score += points.get(lefts.get(val))
            scores.append(score)
    return median(scores)

def median(lst):
    lst.sort()
    mid = len(lst) // 2
    res = (lst[mid] + lst[~mid]) / 2
    return res

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))