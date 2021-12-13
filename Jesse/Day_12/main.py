class Graph:
    def __init__(self):
        self.name_to_node = {}
    
    def to_string(self):
        for name in self.name_to_node.keys():
            print(name, [(node.name, node.small) for node in self.name_to_node[name].adjacent])

class Node:
    def __init__(self, name):
        self.name = name
        self.small = name.islower()
        self.adjacent = []
        
    def set_name(self,name):
        self.name = name
        self.small = name.islower()
        
def has_small_twice(path, graph):
    has = False
    for val in path.split("-"):
        if path.count(val) > 1 and graph.name_to_node.get(val).small == True:
            has = True
    return has
        
def read_and_return_graph():
    lines = [line.strip().split("-") for line in open("input.txt")]
    my_graph = Graph()
    for edge in lines:
        start_node = Node("tmp")
        end_node = Node("tmp")
        if my_graph.name_to_node.get(edge[0]):
            start_node = my_graph.name_to_node.get(edge[0])
        else:
            start_node.set_name(edge[0])
            my_graph.name_to_node[start_node.name] = start_node
        if my_graph.name_to_node.get(edge[1]):
            end_node = my_graph.name_to_node.get(edge[1])
        else:
            end_node.set_name(edge[1])
            my_graph.name_to_node[end_node.name] = end_node
        
        start_node.adjacent.append(end_node)
        end_node.adjacent.append(start_node)
    return my_graph

def part_1():
    my_graph = read_and_return_graph()
    start = my_graph.name_to_node.get("start")
    path_counts = 0
    cur_node = start
    stack = []
    path = "start"
    stack.append(path)
    while len(stack) > 0:
        path = stack.pop()
        cur_name = path.split("-")[len(path.split("-")) - 1]
        cur_node = my_graph.name_to_node.get(cur_name)
        for node in cur_node.adjacent:
            if node.name == "end":
                path_counts += 1
            elif (node.name not in path or not node.small) and node.name != "start":
                stack.append(path + "-" + node.name)

    return path_counts

def part_2():
    my_graph = read_and_return_graph()
    start = my_graph.name_to_node.get("start")
    path_counts = 0
    cur_node = start
    stack = []
    path = "start"
    stack.append(path)
    while len(stack) > 0:
        path = stack.pop()
        cur_name = path.split("-")[len(path.split("-")) - 1]
        cur_node = my_graph.name_to_node.get(cur_name)
        for node in cur_node.adjacent:
            if node.name == "end":
                path_counts += 1
            elif ((not has_small_twice(path, my_graph) and path.count(node.name) < 2) or (has_small_twice(path, my_graph) and path.count(node.name) < 1) or not node.small) and node.name != "start":
                stack.append(path + "-" + node.name)
            
    return path_counts

print("Part 1: " + str(part_1()))
print("Part 2: " + str(part_2()))