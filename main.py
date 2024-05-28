
prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
board_size = int(input(prompt_1))

while not (board_size>=5 and board_size<=9):
    print(error_message_1)
    board_size = int(input(prompt_1))

current_board = [["-" for i in range(board_size)] for k in range(board_size)]
winning_board = [["-" for i in range(board_size)] for k in range(board_size)]
def print_board(board_list):
    first_raw = "  "
    for column_numbers in range(1,len(board_list) +1):
        first_raw = first_raw + f"{column_numbers} "
    print(first_raw[:-1])
    for raw_index in range(len(board_list)):
        print(raw_index + 1,end=" ")
        current_raw = ""
        for column_index in range(len(board_list)):

            current_raw = current_raw + board_list[raw_index][column_index] + " "
        print(current_raw[:-1])

number_of_inputs = int(input(prompt_2))
while not (number_of_inputs>=1 and number_of_inputs<=(board_size**2)):
    print(error_message_2)
    number_of_inputs = int(input(prompt_2))

while number_of_inputs != 0:
    input_lst2 = input(prompt_3)
    input_lst2 = input_lst2.strip().split()
    try:
        raw = int(input_lst2[0])
        column = int(input_lst2[1])
    except:
        print(error_message_3)
        continue
    if not((raw>=1 and raw<=board_size) and (column >= 1 and column <= board_size)):
        print(error_message_4)
        continue
    else:
        if current_board[raw-1][column-1] == "+":
            print(error_message_5)
            continue
        else:
            current_board[raw - 1][column - 1] = "+"
            print_board(current_board)
            number_of_inputs -= 1


while True:

    input_lst2 = input(prompt_4)
    if input_lst2.strip().lower() == "exit":
        print(prompt_6)
        break

    input_lst2 = input_lst2.strip().split()
    try:
        raw = int(input_lst2[0])
        column = int(input_lst2[1])
    except:
        print(error_message_3)
        continue
    if not ((raw >= 1 and raw <= board_size) and (column >= 1 and column <= board_size)):
        print(error_message_4)
        continue
    else:
        if current_board[raw - 1][column - 1] == "+":
            current_board[raw - 1][column - 1] = "-"
        else:
            current_board[raw - 1][column - 1] = "+"
    if (raw-1 >= 1 and raw-1 <= board_size) and (column+1 >= 1 and column+1 <= board_size):
        if current_board[raw - 2][column] == "+":
            current_board[raw - 2][column] = "-"
        else:
            current_board[raw - 2][column] = "+"
    if (raw-1 >= 1 and raw-1 <= board_size) and (column-1 >= 1 and column-1 <= board_size):
        if current_board[raw - 2][column - 2] == "+":
            current_board[raw - 2][column - 2] = "-"
        else:
            current_board[raw - 2][column - 2] = "+"
    if (raw+1 >= 1 and raw+1 <= board_size) and (column+1 >= 1 and column+1 <= board_size):
        if current_board[raw][column] == "+":
            current_board[raw][column] = "-"
        else:
            current_board[raw][column] = "+"
    if (raw+1 >= 1 and raw+1 <= board_size) and (column-1 >= 1 and column-1 <= board_size):
        if current_board[raw][column-2] == "+":
            current_board[raw][column-2] = "-"
        else:
            current_board[raw][column-2] = "+"



    print_board(current_board)
    if current_board == winning_board:
        print(prompt_5)
        print(prompt_6)
        break


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

