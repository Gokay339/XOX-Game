board = [' ' for x in range(10)]

# Function to display the game board.
def display_board():
  print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3])
  print("------------")
  print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6])
  print("------------")
  print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])

# Function to place a letter ('X' or 'O') at a specified position on the board.
def place_letter(letter, position):
  board[position] = letter

# Function to check if a space on the board is empty.
def is_space_empty(position):
  return board[position] == ' '

# Function to check if the game board is full (all spaces are occupied).
def is_board_full():
  if board.count(' ') > 1:
    return False
  else:
    return True

# Function to check if a player with a given letter ('X' or 'O') has won the game.
def is_winner(board, letter):
  return (board[1] == letter and board[2] == letter and board[3] == letter) or \
         (board[4] == letter and board[5] == letter and board[6] == letter) or \
         (board[7] == letter and board[8] == letter and board[9] == letter) or \
         (board[1] == letter and board[4] == letter and board[7] == letter) or \
         (board[2] == letter and board[5] == letter and board[8] == letter) or \
         (board[3] == letter and board[6] == letter and board[9] == letter) or \
         (board[1] == letter and board[5] == letter and board[9] == letter) or \
         (board[3] == letter and board[5] == letter and board[7] == letter)

# Function for player's move.
def player_move():
  position = int(input("Enter a position between 1-9: "))
  if is_space_empty(position):
    place_letter('X', position)
    if is_winner(board, 'X'):
      display_board()
      print("Congratulations! You won.")
      exit()
    display_board()
  else:
    print("The chosen position is already occupied. Please choose another position.")
    player_move()

# Function for computer's move.
def computer_move():
  import random
  available_positions = [position for position, letter in enumerate(board) if letter == ' ' and position != 0]

  move = 0

  for letter in ['O', 'X']:
    for position in available_positions:
      copy_board = board[:]
      copy_board[position] = letter
      if is_winner(copy_board, letter):
        move = position
        return move

  corners = []

  for position in available_positions:
    if position in [1, 3, 7, 9]:
      corners.append(position)

  if len(corners) > 0:
    move = random.choice(corners)
    return move

  if 5 in available_positions:
    move = 5
    return move

  centers = []

  for position in available_positions:
    if position in [2, 4, 6, 8]:
      centers.append(position)

  if len(centers) > 0:
    move = random.choice(centers)
    return move

# Function to start the game.
def game():
  print("Welcome to the XOX Game")
  display_board()

  while not is_board_full():

    player_move()
    if is_board_full():
      print("The game ended in a draw. There is no winner!")
      exit()

    print("-------------------------------")

    computer_move_result = computer_move()
    place_letter('O', computer_move_result)
    if is_winner(board, 'O'):
      display_board()
      print("The computer wins, You lost!")
      exit()

    display_board()
    if is_board_full():
      print("The game ended in a draw. There is no winner!")
      exit()

    print("-------------------------------")

game()
