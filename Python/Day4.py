def open_data(file_name):
    # Open file and separate lines
    with open(file_name, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    # Isolate called numbers
    nums_called = [int(x) for x in lines[0].split(',')]

    # Empty arrays for boards
    all_boards = []
    single_board = []

    # Parse lines to populate board arrays
    for b in lines[2:]:
        row = b.split()

        if row == []:
            all_boards.append(single_board)
            single_board = []
        else:
            row = b.split()
            single_board.append(row)

    return nums_called, all_boards

def check_bingo(board):
    for r in board:
        cnt_marked_rows = len([x for x in r if x == -1])

    for c in range(5):
        cnt_marked_cols = len([x[c] for x in board if x == -1])

    for v in range(5):
        cnt_marked_diag = len([x for x in v])

    if cnt_marked_rows == 5 or cnt_marked_cols == 5:
        return True
    else:
        return False

def main():
    nums_called, all_boards = open_data('./Data/Day04Data.txt')
    winner = False
    
    while winner == False:
        for n in nums_called:
            for b in all_boards:
                for r in b:
                    if str(n) in r:
                        found_index = r.index(str(n))
                        r[found_index] = -1
                
            
                winner = check_bingo(b)

                if winner == True:
                    print(f'Winner after number {n}!')
                    break
                else:
                    print(f'No winner after number {n}!')




main()



