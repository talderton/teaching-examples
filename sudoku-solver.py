def create_board(line_set):

    board = [[0 for row in range(9)] for col in range(9)]
    row = 0;
    col = 0;
    for r in line_set:
        if r != '' and row < 9:
            for n in r:
                board[row][col] = int(n)
                col += 1
            row += 1
            col = 0
    return board


def print_board(board):

    with open('solved_puzzles.txt', 'a+') as f:
        for row in range(len(board)):
            if row % 3 == 0 and row != 0:
                f.write("------+------+------\n")

            for col in range(len(board[0])):
                if col % 3 == 0 and col != 0:
                    f.write("|")

                if col == 8:
                    f.write(str(board[row][col]))
                else:
                    f.write(str(board[row][col]) + " ")
            f.write("\n")

        f.write("----------------------------\n")


def print_error():

    with open('solved_puzzles.txt', 'a+') as f:
        f.write("----------------------------\n")
        f.write("**Puzzle could not be solved**\n")
        f.write("----------------------------\n")


def find_empty(board):

    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return (row, col)
    return None


def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    square_row = pos[1] // 3
    square_col = pos[0] // 3

    for i in range(square_col * 3, square_col * 3):
        for j in range(square_row * 3, square_row * 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

with open('blank_puzzles.txt') as f:
    lines = [line.rstrip() for line in f]
    line_set = []
    for r in lines:
        if r != "":
            line_set.append(r)
        else:
            board = create_board(line_set)
            if solve(board):
                print_board(board)
            else:
                print_error(line_set)
            line_set = []
