from timeit import default_timer as timer
import ast
import math

class Node:
    def __init__(self, left_val = None, right_val = None, parent_node = None):
        self.left = left_val
        self.right = right_val
        self.parent = parent_node
            
    def is_list(self):
        return self.is_list

def tree_to_string(node):
    cur_str = ""
    if isinstance(node.left,int) or isinstance(node.left,float):
        cur_str += "[" + str(node.left) + ","
    else:
        cur_str += "[" + tree_to_string(node.left) + ","
    if isinstance(node.right,int) or isinstance(node.right,float):
        cur_str += str(node.right) + "]"
    else:
        cur_str += tree_to_string(node.right) + "]"
    return cur_str
        
def make_node(left_val, right_val, parent):
    left_node = left_val
    right_node = right_val
    if isinstance(left_val, list):
        left_node = make_node(left_val[0], left_val[1], left_val)
    if isinstance(right_val, list):
        right_node = make_node(right_val[0], right_val[1], right_val)

    cur_node = Node(left_node, right_node, parent)
    if isinstance(left_node, Node):
        left_node.parent = cur_node
    if isinstance(right_node, Node):
        right_node.parent = cur_node
        
    return cur_node

def traverse_and_add_tree_right_to_left(tree, val):
    cur_node = tree
    not_found = True
    while not_found:
        if cur_node.parent == None:
            return
        if cur_node.parent.left == cur_node:
            cur_node = cur_node.parent
            if cur_node.parent == None:
                return
        else:
            if isinstance(cur_node.parent.left, int):
                cur_node.parent.left += val
                return
            cur_node = cur_node.parent.left
            while not isinstance(cur_node.right, int):
                cur_node = cur_node.right
            cur_node.right += val
            not_found = False 
    return

def traverse_and_add_tree_left_to_right(tree, val):
    cur_node = tree
    not_found = True
    while not_found:
        if cur_node.parent == None:
            return
        if cur_node.parent.right == cur_node:
            cur_node = cur_node.parent
            if cur_node.parent == None:
                return
        else:
            if isinstance(cur_node.parent.right, int):
                cur_node.parent.right += val
                return
            cur_node = cur_node.parent.right
            while not isinstance(cur_node.left, int):
                cur_node = cur_node.left
            cur_node.left += val
            not_found = False 
    return

def get_root(node):
    cur_node = node
    while cur_node.parent != None:
        cur_node = cur_node.parent
    return cur_node
            
def explode_node(node):
    traverse_and_add_tree_right_to_left(node, node.left)
    traverse_and_add_tree_left_to_right(node, node.right)
    if node.parent.left == node:
        node.parent.left = 0
    elif node.parent.right == node:
        node.parent.right = 0
    return node

def split_node(node):
    if node.left >= 10:
        new_node = Node(int(math.floor(node.left/2)), int(node.left/2 + node.left%2), node)
        new_node.parent.left = new_node
    elif node.right >= 10:
        new_node = Node(int(math.floor(node.right/2)), int(node.right/2 + node.right%2), node)
        new_node.parent.right = new_node
    return 1

def traverse_left_to_right(tree, depth = 0):
    if (isinstance(tree.left, int) and isinstance(tree.right, int)):
        if depth >= 4:
            return tree
    if isinstance(tree.left, Node):
        return_node = traverse_left_to_right(tree.left, depth + 1)
        if return_node != None:
            return return_node
    if isinstance(tree.right, Node):
        return_node = traverse_left_to_right(tree.right, depth + 1)
        if return_node != None:
            return return_node
    return None

def split_next(tree, depth = 0):
    if isinstance(tree.left, int):
        if tree.left > 9:
            split_node(tree)
            return 1
    if isinstance(tree.left, Node):
        return_node = split_next(tree.left, depth + 1)
        if return_node != None:
            return return_node
    if isinstance(tree.right, int):
        if tree.right > 9:
            split_node(tree)
            return 1
    if isinstance(tree.right, Node):
        return_node = split_next(tree.right, depth + 1)
        if return_node != None:
            return return_node
    return None

def sum_up(lists):
    while True:
        if not isinstance(lists[0], int) and isinstance(lists[1], int):
            return sum_up(lists[0])*3 + lists[1]*2
        if isinstance(lists[0], int) and not isinstance(lists[1], int):
            return lists[0]*3 + sum_up(lists[1])*2
        if isinstance(lists[0], int) and isinstance(lists[1], int):
            return lists[0]*3 + lists[1]*2
        for index,val in enumerate(lists):
            if isinstance(val[0], int) and isinstance(val[1], int):
                lists[index] = 3 * val[0] + 2 * val[1]
            elif isinstance(val[0], int) and not isinstance(val[1], int):
                lists[index] = 3 * val[0] + 2 * sum_up(val[1])
            elif not isinstance(val[0], int) and isinstance(val[1], int):
                lists[index] = 3 * sum_up(val[0]) + 2 * val[1]
            else:
                lists[index] = 3 * sum_up(val[0]) + 2 * sum_up(val[1])

def part_1(piece_one, piece_two):
    start = timer()
    adjacency = [ast.literal_eval(line.strip()) for line in open("input.txt")]
    if piece_one != None or piece_two != None:
        adjacency = [ast.literal_eval(piece_one), ast.literal_eval(piece_two)]
    result = adjacency[0]
    tree = make_node(result[0], result[1], None)
    bad_node = traverse_left_to_right(tree)
    while bad_node != None:
        explode_node(bad_node)
        bad_node = traverse_left_to_right(tree)
    for i in range(1,len(adjacency)):
        new_node = make_node(adjacency[i][0], adjacency[i][1], None)
        tree = Node(tree, new_node, None)
        tree.left.parent = tree
        tree.right.parent = tree
        bad_node = traverse_left_to_right(tree)
        while bad_node != None:
            explode_node(bad_node)
            bad_node = traverse_left_to_right(tree)
        success = split_next(tree)
        while success:
            bad_node = traverse_left_to_right(tree)
            while bad_node != None:
                explode_node(bad_node)
                bad_node = traverse_left_to_right(tree)
            success = split_next(tree)
        
    return sum_up(ast.literal_eval(tree_to_string(tree))), timer() - start
                    
def part_2():
    start = timer()
    adjacency = [line.strip() for line in open("input.txt")]
    max_val,_ = part_1(adjacency[0], adjacency[1])
    for i in range(len(adjacency)):
        for j in range(len(adjacency)):
            if i != j:
                cur_val, _ = part_1(adjacency[i], adjacency[j])
                max_val = max(max_val, cur_val)
    
    return max_val, timer() - start

if __name__ == "__main__":
    part_1_answer, time_1 = part_1(None, None)
    print("Part 1: " + str(part_1_answer) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))