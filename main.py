from colorama import *


def greet():
    print(Fore.CYAN + " -------------------")
    print(" Welcome to Tic Tac Toe ")
    print(" Input format: x y ")
    print(" X - row ")
    print(" Y - colum ")
    print(" -------------------" + Style.RESET_ALL)


def show():
    print()
    print(Fore.BLUE + "   | 0 | 1 | 2 | " + Style.RESET_ALL)
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = Fore.BLUE + f" {i} |" + Style.RESET_ALL + f" {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("         Your move: ").split()

        if len(cords) != 2:
            print(" Enter row and columm ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Enter a number! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Coordinates out of range! ")
            continue

        if field[x][y] != " ":
            print(" The cell is occupied! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Won X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Won 0!!!")
            return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(Fore.LIGHTYELLOW_EX + " Mov X!")
    else:
        print(Fore.LIGHTYELLOW_EX + " Mov 0!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Draw!")
        break
