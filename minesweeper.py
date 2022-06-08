import random

SIZE = 3
MINES = 0
BOARD = []


def display():
    for x in range(SIZE + 1):
        if x == 0:
            print("╔═" + "══╦═" * (SIZE - 1) + "══╗")
        elif x == SIZE:
            print("║   " * (SIZE) + "║")
            print("╚═" + "══╩═" * (SIZE - 1) + "══╝")
        else:
            print("║   " * (SIZE) + "║")
            print("╠═" + "══╬═" * (SIZE - 1) + "══╣")


class Square:

    def __init__(self, x, y):
        self.status = "-"
        self.row = x
        self.column = y
        self.mine = False
        self.neighbours = []


def first_move():
    print("""Where would you like to start?\n
    Enter an x and a y co-ordinate, comma separated, 
    to dig the first square: """)
    t, e = input().split(",")
    x = int(t)
    y = int(e)

    for m in range(MINES):
        place_mines(x, y)


def place_mines(x, y):
    h = random.randint(0, SIZE)
    w = random.randint(0, SIZE)
    if h == y or w == x:
        place_mines(x, y)
    else:
        if BOARD[x][y].status != "💣":
            BOARD[x][y].status = "💣"
        else:
            place_mines(x, y)


def next_turn():
    move = input("Would you like to flag, dig, or quit?").lower()
    if move == "quit":
        print("Thank you, come again.")
        quit(0)
    elif move == "dig":
        dig()
    elif move == "flag":
        flag()
    else:
        print("You'll have to speak up, I'm wearing a towel.")


def flag():
    a, b = input("Supply an x and a y coordinate to flag: ").split(",")
    x = int(a)
    y = int(b)


def startup():
    print("It's Minesweeper, you know how it works. How wide a board do you want?")
    global SIZE
    SIZE = int(input("Give me a size, between 3 and 10 inclusive "))

    if SIZE not in range(3, 11):
        print("Wrong answer bud, try again.")
        quit(0)
    else:
        global MINES
        MINES = int(input("And how many mines do you want? "))

        if MINES >= SIZE ** 2:
            print("Woah, that's too many. Try again.")
            quit(0)
        else:
            # initialise an empty board
            for s in range(SIZE):
                for d in range(SIZE):
                    global BOARD
                    BOARD[s][d] = Square(s, d)
            # link each square to it's neighbours
            for a in range(SIZE):
                for b in range(SIZE):
                    sqr = BOARD[a][b]
                    if a == 0:
                        sqr.neighbours.append(BOARD[a+1][b])
                        if b != SIZE-1:
                            sqr.neighbours.append(BOARD[a+1][b+1])
                        if b != 0:
                            sqr.neighbours.append(BOARD[a][b-1])
                            sqr.neighbours.append(BOARD[a+1][b-1])
                    elif a == SIZE-1:
                        sqr.neighbours.append(BOARD[a-1][b])
                    if b == 0:
                        sqr.neighbours.append(BOARD[a][b+1])
                    elif b == SIZE-1:
                        sqr.neighbours.append(BOARD[a][b-1])
            display()
            first_move()


startup()
while True:
    next_turn()
