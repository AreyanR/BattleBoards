class ChessPiece:
   def __init__(self, color, name, health):
       """
       Initialize a chess piece with its color, name, and health.

       :param color: The color of the chess piece ('white' or 'black').
       :param name: The name of the chess piece.
       :param health: The health points of the chess piece.
       """
       self.color = color
       self.name = name
       self.health = health
       self.special_attack_uses = {}

   def decrease_health(self, damage):
       """
       Decrease the health of the chess piece by the given amount of damage.

       :param damage: The amount of damage to be subtracted from the health.
       """
       self.health -= damage

   def __str__(self):
       """
       Return the symbol representing the chess piece when converted to a string.
       """
       return self.symbol

   def valid_moves(self, row, col, board):
       """
       Return a list of valid moves for the chess piece on the given board at the specified position.

       :param row: The row index of the chess piece on the board.
       :param col: The column index of the chess piece on the board.
       :param board: The chess board as a 2D list.
       :return: A list of valid moves as (row, col) tuples.
       """
       return []

   def attack(self, target_piece, attack_name):
       """
       Perform an attack on the target piece with the specified attack name.

       :param target_piece: The target chess piece to be attacked.
       :param attack_name: The name of the attack to be used.
       :return: True if the attack was successful, False otherwise.
       """
       if attack_name in self.attacks:
           if attack_name in self.special_attack_uses and self.special_attack_uses[attack_name] > 0:
               damage = self.attacks[attack_name]
               target_piece.health -= damage
               self.special_attack_uses[attack_name] -= 1

               if target_piece.health <= 0:
                   return True
               else:
                   return False
           elif attack_name not in self.special_attack_uses:
               print(f"{self.name} doesn't have information on attack: {attack_name}")
               return False
           else:
               if self.special_attack_uses[attack_name] <= 0:
                   print(f"{self.name} has used up all special attack uses for {attack_name}.")
               else:
                   print(f"{self.name} doesn't have any remaining uses of {attack_name}.")
               return False
       else:
           print(f"{self.name} doesn't know the attack: {attack_name}")
           return False


class King(ChessPiece):
   def __init__(self, color):
       super().__init__(color, 'King', health=150)
       self.symbol = 'K' if color == 'white' else 'k'
       self.attacks = {
           'Strike': 30,
       }
       self.special_attacks = {
           'Royal Smash': {
               'damage': 60,
               'uses': 3
           }
       }

   def __str__(self):
       return self.symbol

   def valid_moves(self, row, col, board):
       moves = []
       for i in [-1, 0, 1]:
           for j in [-1, 0, 1]:
               new_row = row + i
               new_col = col + j
               if 0 <= new_row < 8 and 0 <= new_col < 8:
                   moves.append((new_row, new_col))
       return moves


class Rook(ChessPiece):
   def __init__(self, color):
       super().__init__(color, 'Rook', health=200)
       self.symbol = 'R' if color == 'white' else 'r'
       self.attacks = {
           'Arrow Strike': 30,
       }
       self.special_attacks = {
           'Rooks Charge': {
               'damage': 45,
               'uses': 4
           }
       }

   def __str__(self):
       return self.symbol

   def valid_moves(self, row, col, board):
       moves = []
       directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
       for dx, dy in directions:
           for i in range(1, 8):
               new_row, new_col = row + i * dx, col + i * dy
               if 0 <= new_row < 8 and 0 <= new_col < 8:
                   moves.append((new_row, new_col))
               else:
                   break
       return moves


class Bishop(ChessPiece):
   def __init__(self, color):
       super().__init__(color, 'Bishop', health=100)
       self.symbol = 'B' if color == 'white' else 'b'
       self.attacks = {
           'Staff Strike': 30,
       }
       self.special_attacks = {
           'Bishops Curse': {
               'damage': 50,
               'uses': 3
           }
       }

   def __str__(self):
       return self.symbol

   def valid_moves(self, row, col, board):
       moves = []
       directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
       for dx, dy in directions:
           for i in range(1, 8):
               new_row, new_col = row + i * dx, col + i * dy
               if 0 <= new_row < 8 and 0 <= new_col < 8:
                   if board[new_row][new_col] is None:
                       moves.append((new_row, new_col))
                   elif board[new_row][new_col].color != self.color:
                       moves.append((new_row, new_col))
                       break
                   else:
                       break
               else:
                   break
       return moves


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'Queen', health=125)
        self.symbol = 'Q' if color == 'white' else 'q'
        self.attacks = {
            'Highness Kick': 40,
        }
        self.special_attacks = {
            'Queens Wrath': {
                'damage': 80,
                'uses': 2
            }
        }

    def __str__(self):
        return self.symbol

    def valid_moves(self, row, col, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            for i in range(1, 8):
                new_row, new_col = row + i * dx, col + i * dy
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    elif board[new_row][new_col].color != self.color:
                        moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return moves


class Knight(ChessPiece):
   def __init__(self, color):
       super().__init__(color, 'Knight', health=160)
       self.symbol = 'N' if color == 'white' else 'n'
       self.attacks = {
           'Strike': 35,
       }
       self.special_attacks = {
           'Knights Charge': {
               'damage': 55,
               'uses': 3
           }
       }

   def __str__(self):
       return self.symbol

   def valid_moves(self, row, col, board):
       moves = []
       directions = [(2, 1), (1, 2), (-2, 1), (1, -2), (2, -1), (-1, 2), (-2, -1), (-1, -2)]
       for dx, dy in directions:
           new_row, new_col = row + dx, col + dy
           if 0 <= new_row < 8 and 0 <= new_col < 8:
               moves.append((new_row, new_col))
       return moves


class Pawn(ChessPiece):
   def __init__(self, color):
       super().__init__(color, 'Pawn', health=50)
       self.symbol = 'P' if color == 'white' else 'p'
       self.attacks = {
           'Strike': 25,
       }
       self.special_attacks = {
           'Pawn Punch': {
               'damage': 35,
               'uses': 3
           }
       }

   def __str__(self):
       return self.symbol

   def valid_moves(self, row, col, board):
       moves = []

       for i in [-1, 1]:
           new_row = row + i
           new_col = col

           if 0 <= new_row < 8:
               moves.append((new_row, new_col))

               for j in [-1, 1]:
                   new_col = col + j
                   if 0 <= new_col < 8 and board[new_row][new_col] and board[new_row][new_col].color != self.color:
                       moves.append((new_row, new_col))

       return moves


def initialize_board():
    """
    Initialize the chess board with the initial postions.

    :return: The initialized chess board as a 2D list.
    """
    board = [[None for _ in range(8)] for _ in range(8)]
    initial_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
    for col in range(8):
      board[0][col] = initial_pieces[col]('black')
      board[1][col] = Pawn('black')
      board[6][col] = Pawn('white')
      board[7][col] = initial_pieces[col]('white')
    return board


def display_board(board, battle_grid=None):
    """
    Display the current state of the chess board, including the battle grid.

    :param board: The chess board as a 2D list.
    :param battle_grid: The battle grid.
    """
    print("  a b c d e f g h")

    for i, row in enumerate(board):
      print(f"{8 - i} ", end="")
      for piece in row:
          if piece is None:
              print(". ", end="")
          else:
              print(f"\033[1m{piece}\033[0m ", end="")
      print(f"{8 - i}")

    if battle_grid:
      print("\nBattle:")
      for row in battle_grid:
          for cell in row:
              print(cell, end=" ")
          print()
      print("\nPlayers' Health:")
      print("\nPlayers' Moves:")
      print()
    else:
      print("  a b c d e f g h")


def battle_scene(piece1, piece2, board, start_pos, end_pos):
    """
    Simulate a battle scene between two chess pieces and update their health.

    :param piece1: The first chess piece participating in the battle.
    :param piece2: The second chess piece participating in the battle.
    :param board: The chess board as a 2D list.
    :param start_pos: The starting position of the battle.
    :param end_pos: The ending position of the battle.
    :return: The winner of the battle (the surviving piece).
    """
    piece1_name = piece1.name
    piece2_name = piece2.name
    piece1_health = piece1.health
    piece2_health = piece2.health
    piece1_symbol = piece1.symbol
    piece2_symbol = piece2.symbol
    piece1_health = getattr(piece1, 'health', None)
    piece2_health = getattr(piece2, 'health', None)
    piece1_attacks = getattr(piece1, 'attacks', None)
    piece2_attacks = getattr(piece2, 'attacks', None)
    piece1_special_attacks = getattr(piece1, 'special_attacks', None)
    piece2_special_attacks = getattr(piece2, 'special_attacks', None)

    start_row, start_col = convert_to_coordinates(start_pos)
    end_row, end_col = convert_to_coordinates(end_pos)

    if piece1_attacks is not None:
        current_turn = piece1_symbol
    else:
        current_turn = piece2_symbol

    print(f"{piece1_symbol} vs {piece2_symbol}")
    while True:
        if piece1_attacks is not None:
            print(f"White {piece1_name} Attacks:")
            for attack, damage in piece1_attacks.items():
                print(f"1: {attack}: {damage} damage")
            if piece1_special_attacks is not None:
                special_attack_name = list(piece1_special_attacks.keys())[0]
                print(f"2: {special_attack_name}: {piece1_special_attacks[special_attack_name]['damage']} damage ({piece1_special_attacks[special_attack_name]['uses']} uses remaining)")
        print("")

        if piece2_attacks is not None:
            print(f"Black {piece2_name} Attacks:")
            for attack, damage in piece2_attacks.items():
                print(f"1: {attack}: {damage} damage")
            if piece2_special_attacks is not None:
                special_attack_name = list(piece2_special_attacks.keys())[0]
                print(f"2: {special_attack_name}: {piece2_special_attacks[special_attack_name]['damage']} damage ({piece2_special_attacks[special_attack_name]['uses']} uses remaining)")
        print("")

        print(f"{piece1_symbol} Current Health: {piece1_health}")
        print(f"{piece2_symbol} Current Health: {piece2_health}")

        while True:
            attack_choice = input(f"{current_turn}, choose your attack (Type in 1 or 2(special) ): ")
            if attack_choice in ('1', '2'):
                break
            else:
                print("Invalid choice. Please enter '1' for a regular attack or '2' for a special attack.")

        if attack_choice == '1':
            if current_turn == piece1_symbol:
                current_damage = piece1_attacks[list(piece1_attacks.keys())[0]]
            else:
                current_damage = piece2_attacks[list(piece2_attacks.keys())[0]]
        else:
            if current_turn == piece1_symbol:
                special_attack_name = list(piece1_special_attacks.keys())[0]
                current_damage = piece1_special_attacks[special_attack_name]['damage']
                piece1_special_attacks[special_attack_name]['uses'] -= 1
            else:
                special_attack_name = list(piece2_special_attacks.keys())[0]
                current_damage = piece2_special_attacks[special_attack_name]['damage']
                piece2_special_attacks[special_attack_name]['uses'] -= 1

        if current_turn == piece1_symbol:
            piece2_health -= current_damage
        else:
            piece1_health -= current_damage

        piece1.health = max(piece1_health, 0)
        piece2.health = max(piece2_health, 0)

        print(f"{current_turn} deals {current_damage} damage.")
        print(f"{piece1_name} Current Health: {piece1.health}")
        print(f"{piece2_name} Current Health: {piece2.health}")

        if piece1_health <= 0:
            if piece1_symbol in ('K', 'k'):
                print(f"{piece1_symbol} has lost the battle, and the game is over.")
                exit()
            else:
                print(f"{piece2_symbol} wins the battle!")
                return piece2
        elif piece2_health <= 0:
            if piece2_symbol in ('K', 'k'):
                print(f"{piece2_symbol} has lost the battle, and the game is over.")
                exit()
            else:
                print(f"{piece1_symbol} wins the battle!")
                return piece1

        current_turn = piece1_symbol if current_turn == piece2_symbol else piece2_symbol


def convert_to_coordinates(pos):
    """
    Convert a chess position string (e.g., 'e2') to row and column coordinates.

    :param pos: The position string (e.g., 'e2').
    :return: A tuple containing row and column coordinates.
    """
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col


def is_valid_move(start_pos, end_pos, board, current_turn):
    """
   Check if a move from start_pos to end_pos is a valid chess move.

   :param start_pos: The starting position of the move.
   :param end_pos: The ending position of the move.
   :param board: The chess board as a 2D list.
   :param current_turn: The current player's turn ('white' or 'black').
   :return: True if the move is valid, otherwise False.
   """
    start_row, start_col = convert_to_coordinates(start_pos)
    end_row, end_col = convert_to_coordinates(end_pos)

    piece = board[start_row][start_col]

    if not piece:
        print(f"No piece at {start_pos}")
        return False

    if piece.color != current_turn:
        print(f"Wrong turn: It's {current_turn}'s turn but the piece is {piece.color}")
        return False

    if start_pos == end_pos:
        print("Invalid move: Starting and ending positions are the same.")
        return False

    valid_moves = piece.valid_moves(start_row, start_col, board)

    if (end_row, end_col) not in valid_moves:
        print("Invalid move: Not a valid move for the selected piece.")
        return False

    if board[end_row][end_col] and board[end_row][end_col].color == current_turn:
        print("Invalid move: Cannot move to a position occupied by a piece of the same color.")
        return False

    return True


def check_collision(board, start_pos, end_pos):
    """
    Check if there is a collision (piece of the opposite color) between two positions on the chess board.

    :param board: The chess board as a 2D list.
    :param start_pos: The starting position.
    :param end_pos: The ending position.
    :return: True if there is a collision,otherwise False .
    """
    start_row, start_col = convert_to_coordinates(start_pos)
    end_row, end_col = convert_to_coordinates(end_pos)

    start_piece = board[start_row][start_col]
    end_piece = board[end_row][end_col]

    return end_piece is not None and end_piece.color != start_piece.color


def get_move(turn, board, collision=False):
    """
    Get a valid move from the player for their current turn.

    :param turn: The current player's turn ('white' or 'black').
    :param board: The chess board as a 2D list.
    :param collision: Whether collision checking is enabled for the move.
    :return: A tuple containing the starting and ending positions of the move.
    """

    while True:
       move = input(f"{turn.capitalize()}'s turn. Enter your move (e.g., 'e2 e3'): ").strip().lower()

       if not move:
           print("Quitting the game.")
           exit()

       if len(move) != 5 or move[0] not in 'abcdefgh' or move[1] not in '12345678' or move[2] != ' ' or move[3] not in 'abcdefgh' or move[4] not in '12345678':
           print("Invalid input format. Please enter your move in the format 'e2 e3'.")
           continue

       start, end = move.split(' ')

       if is_valid_move(start, end, board, turn):
           if collision and board[convert_to_coordinates(start)[0]][convert_to_coordinates(start)[1]].color == turn:
               return start, end
           elif not collision:
               return start, end
       else:
           print("Invalid move. Please try again.")


def update_board(board, start, end, turn):
    """
    Update the chess board after a valid move is made.

    :param board: The chess board as a 2D list.
    :param start: The starting position of the move.
    :param end: The ending position of the move.
    :param turn: The current player's turn ('white' or 'black').
    """
    start_row, start_col = convert_to_coordinates(start)
    end_row, end_col = convert_to_coordinates(end)
    piece = board[start_row][start_col]

    if board[end_row][end_col] and board[end_row][end_col].color != turn:
        winner = battle_scene(piece, board[end_row][end_col], board, start, end)

        if winner == piece:
            board[end_row][end_col] = piece
            board[start_row][start_col] = None

            # Check if the game is over after the battle
            if is_game_over(board, turn):
                display_board(board)
                print(f"Game over! {turn.capitalize()} wins by defeating the opponent's king.")
                exit()
        else:
            # The opponent won the battle, so the current player's piece is removed
            board[start_row][start_col] = None
    else:
        board[end_row][end_col] = piece
        board[start_row][start_col] = None


def play_game():
    """
    Play a game of chess until it's over.
    """
    board = initialize_board()
    turn = 'white'

    while True:
        display_board(board)

        start, end = get_move(turn, board)

        start_row, start_col = convert_to_coordinates(start)
        end_row, end_col = convert_to_coordinates(end)
        piece1 = board[start_row][start_col]
        piece2 = board[end_row][end_col]

        if piece2 and piece2.color != turn:
            winner = battle_scene(piece1, piece2, board, start, end)

            if winner == piece1:
                board[end_row][end_col] = piece1
                board[start_row][start_col] = None
            else:
                pass

        else:
            update_board(board, start, end, turn)

        if is_game_over(board, turn):
            display_board(board)
            print(f"Game over! {turn.capitalize()} wins by defeating the opponent's king.")
            exit()

        turn = 'black' if turn == 'white' else 'white'


def is_game_over(board, turn):
    """
    Check if the game is over (one of the kings is defeated).

    :param board: The chess board as a 2D list.
    :param turn: The current player's turn ('white' or 'black').
    :return: True if the game is over, False otherwise.
    """

    king_symbol = 'K' if turn == 'black' else 'k'
    for row in board:
       for piece in row:
           if isinstance(piece, King) and piece.symbol == king_symbol:
               return False
    return True


if __name__ == "__main__":
   play_game()
