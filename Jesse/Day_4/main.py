import copy
from timeit import default_timer as timer

def part_1():
    start_t = timer()
    called_nums = open("called.txt").readline().split(",")
    lines = [line.strip().split(" ") for line in open("input.txt")]
    board = []
    boards = []
    for line in lines:
        if line[0] == "":
            boards.append(copy.copy(board))
            board = []
        else:
            board.append(line)

    for num in called_nums:
        for board in boards:
            board = process_board(num, board)
            if is_winner(board):
                answer = get_sum(board)
                return answer*int(num), timer() - start_t
    return -1

def get_sum(board):
    final = 0
    for row in board:
        for val in row:
            if val != -1:
                final += int(val)
    return final

def is_winner(board):
    for row in board:
        if row.count(-1) == len(row):
            return True
    transposed_board = transpose(copy.copy(board))
    for row in transposed_board:
        if row.count(-1) == len(row):
            return True
    
def process_board(num, board):
    for index1,row in enumerate(board):
        for index2,val in enumerate(row):
            if val == num:
                board[index1][index2] = -1
    return board

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T
            

def part_2():
    start_t = timer()
    called_nums = open("called.txt").readline().split(",")
    lines = [line.strip().split(" ") for line in open("input.txt")]
    board = []
    boards = []
    for line in lines:
        if line[0] == "":
            boards.append(copy.copy(board))
            board = []
        else:
            board.append(line)

    for num in called_nums:
        new_boards = []
        for board in boards:
            board = process_board(num, board)
            if not is_winner(board):
                new_boards.append(board)
        if len(boards) == 1 and is_winner(boards[0]):
            result = get_sum(boards[0])
            return result*int(num), timer() - start_t
        boards = new_boards
    return -1

if __name__ == "__main__":
    part_1, time_1 = part_1()
    print("Part 1: " + str(part_1) + " in " + str(time_1))
    part_2, time_2 = part_2()
    print("Part 2: " + str(part_2) + " in " + str(time_2))