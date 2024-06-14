board = []
win_board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
for i in range(3):
    board.append([])
    for j in range(3):
        board[i].append([])
        for k in range(3):
            board[i][j].append([])
            for l in range(3):
                board[i][j][k].append(' ')                
def print_board():
    for i in range(3):
        for j in range(3):
            t = []
            for k in range(3):
                t.append(board[i][k][j])
            print(t)
            print(" ")
        print('---------------------------------------------------')
    for i in range(3):
        print(win_board[i])
selected_board = None
selected_in_board = None
player = 'x'
def select_board():
    s = input(player + "'s turn. Select playing board in Row, Column (ex. 0 2 = bottom left): ").split(" ")
    if len(s) == 2:
        if s[0].isnumeric() and s[1].isnumeric():
            if int(s[0]) <= 2 and int(s[1]) <= 2 and int(s[0]) >= 0 and int(s[1]) >= 0:
                if check_board_free(s):
                    return s
                else:
                    print('Board taken')
                    return select_board()
            else:
                print('Out of range')
                return select_board()
        else:
            print('Requires 2 numbers seperated by a space')
            return select_board()
    else:
        print('Requires 2 numbers seperated by a space')
        return select_board()
def select_in_board(): 
    s = input(player + "'s turn. Row, Column (ex. 0 2 = bottom left): ").split(" ")
    if len(s) == 2:
        if s[0].isnumeric() and s[1].isnumeric():
            if int(s[0]) <= 2 and int(s[1]) <= 2 and int(s[0]) >= 0 and int(s[1]) >= 0:
                if check_space(s):
                    return s
                else:
                    print('Spot taken')
                    return select_in_board()
            else:
                print('Out of range') 
                return select_in_board()
        else:
            print('Requires 2 numbers seperated by a space')
            return select_in_board()
    else:
        print('Requires 2 numbers seperated by a space')
        return select_in_board()
def check_board_free(s):
    for k in range(3):
        if " " in board[int(s[0])][int(s[1])][k]:
            return True
    return False
def check_space(sib):
    global selected_board
    if board[int(selected_board[0])][int(selected_board[1])][int(sib[0])][int(sib[1])] == " ":
        return True
    else:
        return False
def full():
    global player
    global selected_board
    global selected_in_board
    selected_board = select_board()
    selected_in_board = select_in_board()
    board[int(selected_board[0])][int(selected_board[1])][int(selected_in_board[0])][int(selected_in_board[1])] = player
    check_win()
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    selected_board = selected_in_board
    print_board()
def half():
    global player
    global selected_board
    global selected_in_board
    selected_in_board = select_in_board()
    board[int(selected_board[0])][int(selected_board[1])][int(selected_in_board[0])][int(selected_in_board[1])] = player
    check_win()
    if player == 'x':
        player = 'o'
    else:
        player = 'x'
    selected_board = selected_in_board
    print_board()
def clear():
    for k in range(3):
        for l in range(3):
            if " " == board[int(selected_board[0])][int(selected_board[1])][k][l]:
                board[int(selected_board[0])][int(selected_board[1])][k][l] = "-"
def check_win():
    recent = board[int(selected_board[0])][int(selected_board[1])][int(selected_in_board[0])][int(selected_in_board[1])]
    t = board[int(selected_board[0])][int(selected_board[1])]
    k = int(selected_in_board[0])
    l = int(selected_in_board[1])
    if (
        (t[k-2][l] == recent and t[k-1][l] == recent) #vertical
        or (t[k][l-2] == recent and t[k][l-1] == recent) #horizontal
        or (t[k-2][l-1] == recent and t[k-1][l-2] == recent) #forward slash
        or (t[k-2][l-2] == recent and t[k-1][l-1] == recent) #backslash
    ): 
        win_board[int(selected_board[0])][int(selected_board[1])] = recent
        check_win_small(win_board[int(selected_board[0])][int(selected_board[1])])
        clear()
def check_win_small(recent):
    t = win_board
    k = int(selected_board[0])
    l = int(selected_board[1])
    if (
        (t[k-2][l] == recent and t[k-1][l] == recent) #vertical
        or (t[k][l-2] == recent and t[k][l-1] == recent) #horizontal
        or (t[k-2][l-1] == recent and t[k-1][l-2] == recent) #forward slash
        or (t[k-2][l-2] == recent and t[k-1][l-1] == recent) #backslash
    ): 
        print_board()
        print(player + " wins")
        exit()
print_board()
full()
while True:
    if not(' ' in board[int(selected_board[0])][int(selected_board[1])][int(selected_in_board[0])]): #check is broken
        full()
    else:
        half()
    
    
