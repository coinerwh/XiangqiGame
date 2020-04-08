# Author: Wil Coiner
# Date: 2/26/20
# Description: Xiangqi game with all of the game mechanics, move validation, check and checkmate/stalemate validations built in
# Along with a game engine that prints the board and asks the user for move input



from colorama import Fore, Back, Style


#### Game Piece Classes ####

class GamePiece:
    """Represents a game piece"""

    def __init__(self, x, y, piece_type, side):
        self._x = x # Game piece location on board
        self._y = y
        self._piece_type = piece_type # Name of game piece
        self._side = side # Whether piece is on black or red side
        self._captured = False # Whether piece is captured or not
        self._name = ''

    def get_x_position(self):
        """Returns x position of piece"""
        return self._x

    def get_y_position(self):
        """Returns y position of piece"""
        return self._y

    def get_piece_type(self):
        """Returns piece type"""
        return self._piece_type

    def get_side(self):
        """Returns side piece is on"""
        return self._side

    def get_capture_status(self):
        """Returns capture status of piece"""
        return self._captured

    def update_position(self,x, y):
        """Updates position of piece"""
        self._x = x
        self._y = y

    def captured(self):
        """Sets status of piece to captured and removes piece from board"""
        # Ensure update is Boolean value
        self._captured = True
        self._position = None

    def get_name(self):
        """Returns name of piece"""
        return self._name


class Empty(GamePiece):
    """Represents empty place on board"""
    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Empty"

class Soldier(GamePiece):
    """Represents a Solder game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Soldier"

class Cannon(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Cannon"

class Chariot(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Chariot"

class Horse(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Horse"

class Elephant(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Elephant"

class Adviser(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "Adviser"

class General(GamePiece):
    """Represents a Cannon game piece"""

    def __init__(self, x, y, piece_type, side):
        super().__init__(x, y, piece_type, side)
        self._name = "General"



### Game Board Class ###

class GameBoard:
    """Represents gameboard for Xiangqi"""
    def __init__(self):
        self._board = [[Empty(x='', y='', piece_type='[ ]', side='')] * 9 for _ in range(10)]
        self._board[3][0] = Soldier(1, 4, "[S]", "Red")
        self._board[3][2] = Soldier(3, 4, "[S]", "Red")
        self._board[3][4] = Soldier(5, 4, "[S]", "Red")
        self._board[3][6] = Soldier(7, 4, "[S]", "Red")
        self._board[3][8] = Soldier(9, 4, "[S]", "Red")
        self._board[2][1] = Cannon(2, 3, "[N]", "Red")
        self._board[2][7] = Cannon(8, 3, "[N]", "Red")
        self._board[0][0] = Chariot(1, 1, "[C]", "Red")
        self._board[0][8] = Chariot(9, 1, "[C]", "Red")
        self._board[0][1] = Horse(2, 1, "[H]", "Red")
        self._board[0][7] = Horse(8, 1, "[H]", "Red")
        self._board[0][2] = Elephant(3, 1, "[E]", "Red")
        self._board[0][6] = Elephant(7, 1, "[E]", "Red")
        self._board[0][3] = Adviser(4, 1, "[A]", "Red")
        self._board[0][5] = Adviser(6, 1, "[A]", "Red")
        self._board[0][4] = General(5, 1, "[G]", "Red")
        self._board[6][0] = Soldier(1, 7, "[S]", "Black")
        self._board[6][2] = Soldier(3, 7, "[S]", "Black")
        self._board[6][4] = Soldier(5, 7, "[S]", "Black")
        self._board[6][6] = Soldier(7, 7, "[S]", "Black")
        self._board[6][8] = Soldier(9, 7, "[S]", "Black")
        self._board[7][1] = Cannon(2, 8, "[N]", "Black")
        self._board[7][7] = Cannon(8, 8, "[N]", "Black")
        self._board[9][0] = Chariot(1, 10, "[C]", "Black")
        self._board[9][8] = Chariot(9, 10, "[C]", "Black")
        self._board[9][1] = Horse(2, 10, "[H]", "Black")
        self._board[9][7] = Horse(8, 10, "[H]", "Black")
        self._board[9][2] = Elephant(3, 10, "[E]", "Black")
        self._board[9][6] = Elephant(7, 10, "[E]", "Black")
        self._board[9][3] = Adviser(4, 10, "[A]", "Black")
        self._board[9][5] = Adviser(6, 10, "[A]", "Black")
        self._board[9][4] = General(5, 10, "[G]", "Black")

    def get_board(self):
        """Returns game board"""
        return self._board

    def get_piece(self, x, y):
        """Returns piece at given location"""
        return self._board[y - 1][x - 1]

    def get_general(self, side):
        """Returns general for side requested"""
        for row in self._board:
            for piece in row:
                if piece.get_name() == 'General' and piece.get_side() == side:
                    return piece

    def print_board(self):
        """Prints game board"""
        print(" a   b   c   d   e   f   g   h   i")
        for i in range(10):
            if i == 5:
                print(Fore.BLUE + "~~~~~~~~~~~~~~ River ~~~~~~~~~~~~~~" + Style.RESET_ALL)
            for j in range(9):
                if self._board[i][j].get_side() == "Black":
                    print (Fore.BLUE + self._board[i][j].get_piece_type(), end=' ' + Style.RESET_ALL)
                elif self._board[i][j].get_side() == "Red":
                    print(Fore.RED + self._board[i][j].get_piece_type(), end=' ' + Style. RESET_ALL)
                else:
                    print(self._board[i][j].get_piece_type(), end=' ')
            print('',i + 1)



### Xiangqi Game Class###

class XiangqiGame:
    """Represents the game engine of chinese chess"""
    def __init__(self):
        self._playersturn = "Red"
        self._gameboard = GameBoard()
        self._gamestate = "UNFINISHED"

    def get_game_board(self):
        """Returns game board"""
        return self._gameboard

    def get_game_state(self):
        """Returns current state of game"""
        return self._gamestate

    def convert_notation(self, x):
        """Converts algebraic to graph notation"""

        pos = str(x)
        notation_dict = {"a": 1,
                          "b": 2,
                          "c": 3,
                          "d": 4,
                          "e": 5,
                          "f": 6,
                          "g": 7,
                          "h": 8,
                          "i": 9,
                          "1": "a",
                          "2": "b",
                          "3": "c",
                          "4": "d",
                          "5": "e",
                          "6": "f",
                          "7": "g",
                          "8": "h",
                          "9": "i",
                          }
        return notation_dict[pos]


    def make_move(self, move_from, move_to):
        """Moves game piece if valid"""
        from_x = int(self.convert_notation(move_from[0]))
        from_y = int(move_from[1:])
        to_x = int(self.convert_notation(move_to[0]))
        to_y = int(move_to[1:])
        try:
            current_piece = self._gameboard._board[from_y - 1][from_x - 1]
            move_to_piece = self._gameboard._board[to_y - 1][to_x - 1]
            piece_name = current_piece.get_name()
            piece_side = current_piece.get_side()
            if piece_side == "Black":
                other_side = "Red"
            else:
                other_side = "Black"
        except IndexError: # Call is out of bounds
            print("Out of Bounds")
            return False

        if current_piece.get_side() != self._playersturn: # Checks player turn
            print("Wrong turn")
            return False
        elif current_piece.get_side() == move_to_piece.get_side(): # Capturing same side
            print(move_to_piece.get_name())
            print(move_to_piece.get_side())
            print(current_piece.get_side())
            print("Would capture same side piece")
            return False
        elif piece_name == "Soldier" and not self.check_soldier_move(to_x, to_y, current_piece):
            print("Bad soldier")
            return False
        elif piece_name == "Cannon" and not self.check_cannon_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            print("Bad cannon")
            return False
        elif piece_name == "Chariot" and not self.check_chariot_move(from_x, from_y, to_x, to_y, current_piece):
            print("Bad chariot")
            return False
        elif piece_name == "Horse" and not self.check_horse_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            print("Bad horse")
            return False
        elif piece_name == "Elephant" and not self.check_elephant_move(from_x, from_y, to_x, to_y, current_piece):
            print("Bad elephant")
            return False
        elif piece_name == "Adviser" and not self.check_adviser_move(from_x, from_y, to_x, to_y, current_piece):
            print("Bad advisor")
            return False
        elif piece_name == "General" and not self.check_general_move(from_x, from_y, to_x, to_y, current_piece):
            print("Bad general")
            return False
        elif piece_name == "Empty":
            print("Empty space")
            return False
        elif self._gamestate != "UNFINISHED": # Check to see if game over
            return False
        else:
            self._gameboard._board[to_y - 1][to_x - 1] = current_piece # Moves piece to new place
            current_piece.update_position(to_x, to_y) # Updates position of piece
            self._gameboard._board[from_y - 1][from_x - 1] = Empty(x='', y='', piece_type='[ ]', side='') # Replaces old place with Empty
            if self.is_in_check(current_piece.get_side()): # if friendly move checks general
                print("This will leave general in check")
                self._gameboard._board[from_y - 1][from_x - 1] = current_piece  # Moves piece back
                current_piece.update_position(from_x, from_y)  # reverses position of piece to original
                self._gameboard._board[to_y - 1][to_x - 1] = move_to_piece
                return False
            elif self.is_in_check(other_side):
                print(other_side, "is in check")
                if self.check_mate(other_side): # Checkmate
                    self._gamestate = piece_side.upper() + "_WON"
                    if self._playersturn == "Red":
                        self._playersturn = "Black"
                    else:
                        self._playersturn = "Red"
                    return True
                elif self._playersturn == "Red":
                    self._playersturn = "Black"
                else:
                    self._playersturn = "Red"
                return True
            elif self.check_mate(other_side): # Stalemate
                self._gamestate = piece_side.upper() + "_WON"
                if self._playersturn == "Red":
                    self._playersturn = "Black"
                else:
                    self._playersturn = "Red"
                return True
            elif self._playersturn == "Red":
                self._playersturn = "Black"
            else:
                self._playersturn = "Red"
            return True

    def make_move_test(self, move_from, move_to):
        """Tests if move is valid"""
        from_x = int(self.convert_notation(move_from[0]))
        from_y = int(move_from[1:])
        to_x = int(self.convert_notation(move_to[0]))
        to_y = int(move_to[1:])
        try:
            current_piece = self._gameboard._board[from_y - 1][from_x - 1]
            move_to_piece = self._gameboard._board[to_y - 1][to_x - 1]
            piece_name = current_piece.get_name()
        except IndexError: # Call is out of bounds
            return False

        if current_piece.get_side() == move_to_piece.get_side(): # Capturing same side
            return False
        elif piece_name == "Soldier" and not self.check_soldier_move(to_x, to_y, current_piece):
            return False
        elif piece_name == "Cannon" and not self.check_cannon_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            return False
        elif piece_name == "Chariot" and not self.check_chariot_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Horse" and not self.check_horse_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            return False
        elif piece_name == "Elephant" and not self.check_elephant_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Adviser" and not self.check_adviser_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "General" and not self.check_general_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Empty":
            return False
        elif self._gamestate != "UNFINISHED": # Check to see if game over
            return False
        else:
            return True

    def legal_and_check_test(self, move_from, move_to):
        """Tests if move is valid and keeps general in check"""
        from_x = int(self.convert_notation(move_from[0]))
        from_y = int(move_from[1:])
        to_x = int(self.convert_notation(move_to[0]))
        to_y = int(move_to[1:])
        try:
            current_piece = self._gameboard._board[from_y - 1][from_x - 1]
            move_to_piece = self._gameboard._board[to_y - 1][to_x - 1]
            piece_name = current_piece.get_name()
        except IndexError: # Call is out of bounds
            return False

        if current_piece.get_side() == move_to_piece.get_side(): # Capturing same side
            return False
        elif piece_name == "Soldier" and not self.check_soldier_move(to_x, to_y, current_piece):
            return False
        elif piece_name == "Cannon" and not self.check_cannon_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            return False
        elif piece_name == "Chariot" and not self.check_chariot_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Horse" and not self.check_horse_move(from_x, from_y, to_x, to_y, current_piece, move_to_piece):
            return False
        elif piece_name == "Elephant" and not self.check_elephant_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Adviser" and not self.check_adviser_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "General" and not self.check_general_move(from_x, from_y, to_x, to_y, current_piece):
            return False
        elif piece_name == "Empty":
            return False
        elif self._gamestate != "UNFINISHED": # Check to see if game over
            return False
        else:
            self._gameboard._board[to_y - 1][to_x - 1] = current_piece # Moves piece to new place
            current_piece.update_position(to_x, to_y) # Updates position of piece
            self._gameboard._board[from_y - 1][from_x - 1] = Empty(x='', y='', piece_type='[ ]', side='') # Replaces old place with Empty
            if self.is_in_check(current_piece.get_side()): # if move checks general
                self._gameboard._board[from_y - 1][from_x - 1] = current_piece  # Moves piece back
                current_piece.update_position(from_x, from_y)  # reverses position of piece to original
                self._gameboard._board[to_y - 1][to_x - 1] = move_to_piece
                return False
            else:
                self._gameboard._board[from_y - 1][from_x - 1] = current_piece  # Moves piece back
                current_piece.update_position(from_x, from_y)  # reverses position of piece to original
                self._gameboard._board[to_y - 1][to_x - 1] = move_to_piece
                return True

    def is_in_check(self, check_side):
        """Checks whether player is in check"""
        side = check_side.capitalize()
        general = self._gameboard.get_general(side)
        general_pos = str(self.convert_notation(general.get_x_position())) + str(general.get_y_position())
        check_counter = 0

        for row in self._gameboard.get_board():
            for piece in row:
                if piece.get_side() == side or piece.get_name() == "Empty":
                    continue
                else:
                    current_x = str(self.convert_notation(piece.get_x_position()))
                    current_y = str(piece.get_y_position())
                    if self.make_move_test(current_x + current_y, general_pos):
                        check_counter += 1
                    else:
                        continue
        if check_counter > 0:
            return True
        else:
            return False

    def check_mate(self, check_side):
        """Checks to see if side is in checkmate"""
        moves_list = ['a1','b1','c1','d1','e1','f1','g1','h1','i1','a2','b2','c2','d2','e2','f2','g2','h2','i2','a3','b3','c3','d3','e3','f3','g3','h3','i3','a4','b4','d4','e4','f4','g4','h4','i4','a5','b5','c5','d5','e5','f5','g5','h5','i5','a6','b6','c6','d6','e6','f6','g6','h6','i6','a7','b7','c7','d7','e7','f7','g7','h7','i7','a8','b8','c8','d8','e8','f8','g8','h8','i8','a9','b9','c9','d9','e9','f9','g9','h9','i9','a10','b10','c10','d10','e10','f10','g10','h10','i10']
        side = check_side.capitalize()
        general = self._gameboard.get_general(side)
        general_pos = str(self.convert_notation(general.get_x_position())) + str(general.get_y_position())
        check_counter = 0

        for row in self._gameboard.get_board():
            for piece in row:
                if piece.get_side() != side or piece.get_name() == "Empty":
                    continue
                else:
                    current_pos_x = piece.get_x_position()
                    current_pos_y = piece.get_y_position()
                    current_pos = str(self.convert_notation(current_pos_x)) + str(current_pos_y)
                    for move_to in moves_list:
                        if not self.legal_and_check_test(current_pos, move_to):
                            continue
                        else:
                            check_counter += 1
        if check_counter == 0:
            print(side + " has lost.")
            return True
        else:
            return False

    def check_soldier_move(self, x_to, y_to, current_piece, move_to_piece=""):
        """Checks whether move is valid for soldier"""
        if x_to > 9 or x_to < 1 or y_to > 10 or y_to < 1: # Checks to make sure move is inside game board
            return False
        elif current_piece.get_side() == 'Red': # Check valid Red side move
            if current_piece.get_y_position() < 6: # Before river
                if x_to != current_piece.get_x_position(): # x position changes before river
                    return False
                elif y_to != current_piece.get_y_position() + 1:  # Red y change only positive 1
                    return False
                elif (x_to == current_piece.get_x_position() + 1 or x_to == current_piece.get_x_position() - 1) and y_to == current_piece.get_y_position() + 1:
                    return False  # move is diagonal and not just forward or sideways
                else:
                    return True
            elif x_to != current_piece.get_x_position() + 1 and x_to != current_piece.get_x_position() - 1 and x_to != current_piece.get_x_position(): # After river x change only 1
                return False
            elif y_to != current_piece.get_y_position() + 1 and y_to != current_piece.get_y_position(): # Red y change only positive 1
                return False
            elif (x_to == current_piece.get_x_position() + 1 or x_to == current_piece.get_x_position() - 1) and y_to == current_piece.get_y_position() + 1:
                return False # move is diagonal and not just forward or sideways
            else:
                return True
        elif current_piece.get_side() == 'Black': # Black side move
            if current_piece.get_y_position() > 5:  # Before river
                if x_to != current_piece.get_x_position():  # x position changes before river
                    return False
                elif y_to != current_piece.get_y_position() - 1:  # Red y change only positive 1
                    return False
                elif (x_to == current_piece.get_x_position() + 1 or x_to == current_piece.get_x_position() - 1) and y_to == current_piece.get_y_position() - 1:
                    return False  # move is diagonal and not just forward or sideways
                else:
                    return True
            elif x_to == current_piece.get_x_position() + 1 and x_to == current_piece.get_x_position() - 1 and x_to != current_piece.get_x_position():  # After river x change only 1
                return False
            elif y_to != current_piece.get_y_position() - 1 and y_to != current_piece.get_y_position():  # Black y change only negative 1
                return False
            elif (x_to == current_piece.get_x_position() + 1 or x_to == current_piece.get_x_position() - 1) and y_to == current_piece.get_y_position() - 1:
                return False  # move is diagonal and not just forward or sideways
            else:
                return True
        else: # No piece
            return False

    def check_chariot_move(self, x_from, y_from, x_to, y_to, current_piece):
        """Check whether move is valid for chariot"""
        count = 0
        if x_to > 9 or x_to < 1 or y_to > 10 or y_to < 1: # Checks to make sure move is inside game board
            return False
        elif x_from != x_to and y_to != y_from: # Diagonal move
            return False
        elif x_to == x_from and y_to < y_from:  # Negative Vertical move
            for index in range(1, current_piece.get_y_position() - y_to):
                if self._gameboard._board[(y_from - 1) - index][x_from - 1].get_name() != "Empty":
                    count += 1
            if count != 0:  # Can only jump 1 piece
                return False
            else:
                return True
        elif x_to == x_from and y_to > y_from:  # Positive Vertical move
            for index in range(1, y_to - current_piece.get_y_position()):
                if self._gameboard._board[(y_from - 1) + index][x_from - 1].get_name() != "Empty":
                    count += 1
            if count != 0:
                return False
            else:
                return True
        elif y_to == y_from and x_to > x_from:  # Positive horizontal move
            for index in range(1, x_to - current_piece.get_x_position()):
                if self._gameboard._board[(y_from - 1)][(x_from - 1) + index].get_name() != "Empty":
                    count += 1
            if count != 0:
                return False
            else:
                return True
        elif y_to == y_from and x_to < x_from:  # Negative horizontal move
            for index in range(1, current_piece.get_x_position() - x_to):
                if self._gameboard._board[(y_from - 1)][(x_from - 1) - index].get_name() != "Empty":
                    count += 1
            if count != 0:
                return False
            else:
                return True

    def check_cannon_move(self, x_from, y_from, x_to, y_to, current_piece, move_to_piece):
        """Checks whether move is valid for cannon"""
        count = 0
        if x_to > 9 or x_to < 1 or y_to > 10 or y_to < 1: # Checks to make sure move is inside game board
            return False
        elif x_from != x_to and y_to != y_from: # Diagonal move
            return False
        elif move_to_piece.get_piece_type() != "[ ]": # if move tries to capture enemy piece
            if x_to == x_from and y_to < y_from: # Negative Vertical move
                for index in range(1, current_piece.get_y_position() - y_to):
                    if self._gameboard._board[(y_from - 1) - index][x_from - 1].get_name() != "Empty":
                        count += 1
                if count != 1: # Can only jump 1 piece
                    return False
                else:
                    return True
            elif x_to == x_from and y_to > y_from: # Positive Vertical move
                for index in range(1, y_to - current_piece.get_y_position()):
                    if self._gameboard._board[(y_from - 1) + index][x_from - 1].get_name() != "Empty":
                        count += 1
                if count != 1:
                    return False
                else:
                    return True
            elif y_to == y_from and x_to > x_from: # Positive horizontal move
                for index in range(1, x_to - current_piece.get_x_position()):
                    if self._gameboard._board[(y_from - 1)][(x_from - 1) + index].get_name() != "Empty":
                        count += 1
                if count != 1:
                    return False
                else:
                    return True
            elif y_to == y_from and x_to < x_from: # Negative horizontal move
                for index in range(1,current_piece.get_x_position() - x_to):
                    if self._gameboard._board[(y_from - 1)][(x_from - 1) - index].get_name() != "Empty":
                        count += 1
                if count != 1:
                    return False
                else:
                    return True
        elif not self.check_chariot_move(x_from, y_from, x_to, y_to, current_piece):
            return False
        else:
            return True

    def check_adviser_move(self, x_from, y_from, x_to, y_to, current_piece,):
        """Checks whether move is valid for adviser"""
        if current_piece.get_side() == "Red": # Red piece
            if x_to > 6 or x_to < 4 or y_to > 3 or y_to < 1:  # Stays in palace
                return False
            elif x_from == x_to or y_from == y_to:  # Move is not diagonal
                return False
            elif (x_to - x_from) > 1 or (x_from - x_to) > 1 or (y_to - y_from) > 1 or (y_from - y_to) > 1:  # More than one place diagonally
                return False
            else:
                return True
        elif current_piece.get_side() == "Black": # Black piece
            if x_to > 6 or x_to < 4 or y_to > 10 or y_to < 8:  # Stays in palace
                return False
            elif x_from == x_to or y_from == y_to:  # Move is not diagonal
                return False
            elif (x_to - x_from) > 1 or (x_from - x_to) > 1 or (y_to - y_from) > 1 or (y_from - y_to) > 1:  # More than one place diagonally
                return False
            else:
                return True

    def check_general_move(self, x_from, y_from, x_to, y_to, current_piece):
        """Check whether move is valid for adviser"""
        count = 0
        if current_piece.get_side() == "Black":
            red_general = self._gameboard.get_general("Red")
            if current_piece.get_x_position() == red_general.get_x_position(): # Checking to see if there is straight path to enemy general
                for index in range(1, (current_piece.get_y_position() - red_general.get_y_position())):
                    if self._gameboard._board[(y_from - 1) - index][(x_from - 1)].get_name() != "Empty":
                        count += 1
                if count == 0: # Flying General check (must be intervening piece between two generals)
                    return False
                elif (x_to - x_from) > 1 or (x_from - x_to) > 1:  # x change <= 1
                    return False
                elif (y_to - y_from) > 1 or (y_from - y_to) > 1:  # y change <= 1
                    return False
                elif x_to != x_from and y_to != y_from:
                    return False  # move is diagonal and not just forward or sideways
                else:
                    return True
            elif (x_to - x_from) > 1 or (x_from - x_to) > 1:  # x change <= 1
                return False
            elif (y_to - y_from) > 1 or (y_from - y_to) > 1:  # y change <= 1
                return False
            elif x_to != x_from and y_to != y_from:
                return False  # move is diagonal and not just forward or sideways
            else:
                return True
        elif current_piece.get_side() == "Red":
            black_general = self._gameboard.get_general("Black")
            if current_piece.get_x_position() == black_general.get_x_position(): # Checking to see if there is straight path to enemy general
                for index in range(1, (black_general.get_y_position() - current_piece.get_y_position())):
                    if self._gameboard._board[(y_from - 1) + index][(x_from - 1)].get_name() != "Empty":
                        count += 1
                if count == 0: # Flying General check (must be intervening piece between two generals)
                    return False
                elif (x_to - x_from) > 1 or (x_from - x_to) > 1:  # x change <= 1
                    return False
                elif (y_to - y_from) > 1 or (y_from - y_to) > 1:  # y change <= 1
                    return False
                elif x_to != x_from and y_to != y_from:
                    return False  # move is diagonal and not just forward or sideways
                else:
                    return True
            elif (x_to - x_from) > 1 or (x_from - x_to) > 1:  # x change <= 1
                return False
            elif (y_to - y_from) > 1 or (y_from - y_to) > 1:  # y change <= 1
                return False
            elif x_to != x_from and y_to != y_from:
                return False  # move is diagonal and not just forward or sideways
            else:
                return True

    def check_elephant_move(self, x_from, y_from, x_to, y_to, current_piece):
        """Check whether move is valid for elephant"""
        if current_piece.get_side() == "Red":
            if x_to > 9 or x_to < 1 or y_to > 5 or y_to < 1:  # Checks to make sure move is inside defensive area
                return False
            elif x_from == x_to or y_from == y_to:  # Move is not diagonal
                return False
            elif ((y_to - y_from) != 2 or (x_to - x_from) != 2) and ((y_to - y_from) != 2 or (x_from - x_to) != 2) and ((y_from - y_to) != 2 or (x_from - x_to) != 2) and ((y_from - y_to) != 2 or (x_to - x_from) != 2): # Moves 2 diagonally
                return False
            elif (x_to - x_from) > 0 and (y_to - y_from) > 0: # Positive vertical and horizontal move
                if (self._gameboard._board[y_to - 2][x_to - 2]).get_name() != "Empty": # Intervening piece
                    return False
                else:
                    return True
            elif (x_from - x_to) > 0 and (y_from - y_to) > 0: # Negative vertical and horizontal move
                if (self._gameboard._board[y_to][x_to]).get_name() != "Empty": # Intervening piece
                    return False
                else:
                    return True
            elif (x_to - x_from) > 0 and (y_from - y_to) > 0:  # Negative vertical and positive horizontal move
                if (self._gameboard._board[y_to][x_to - 2]).get_name() != "Empty":  # Intervening piece
                    return False
                else:
                    return True
            elif (x_from - x_to) > 0 and (y_to - y_from) > 0:  # Positive vertical and negative horizontal move
                if (self._gameboard._board[y_to - 2][x_to]).get_name() != "Empty":  # Intervening piece
                    return False
                else:
                    return True
        elif current_piece.get_side() == "Black":
            if x_to > 9 or x_to < 1 or y_to > 10 or y_to < 6:  # Checks to make sure move is inside defensive area
                return False
            elif x_from == x_to or y_from == y_to:  # Move is not diagonal
                return False
            elif ((y_to - y_from) != 2 or (x_to - x_from) != 2) and ((y_to - y_from) != 2 or (x_from - x_to) != 2) and ((y_from - y_to) != 2 or (x_from - x_to) != 2) and ((y_from - y_to) != 2 or (x_to - x_from) != 2): # Moves 2 diagonally
                return False
            elif (x_to - x_from) > 0 and (y_to - y_from) > 0: # Positive vertical and horizontal move
                if (self._gameboard._board[y_to - 2][x_to - 2]).get_name() != "Empty": # Intervening piece
                    return False
                else:
                    return True
            elif (x_from - x_to) > 0 and (y_from - y_to) > 0: # Negative vertical and horizontal move
                if (self._gameboard._board[y_to][x_to]).get_name() != "Empty": # Intervening piece
                    return False
                else:
                    return True
            elif (x_to - x_from) > 0 and (y_from - y_to) > 0:  # Negative vertical and positive horizontal move
                if (self._gameboard._board[y_to][x_to - 2]).get_name() != "Empty":  # Intervening piece
                    return False
                else:
                    return True
            elif (x_from - x_to) > 0 and (y_to - y_from) > 0:  # Positive vertical and negative horizontal move
                if (self._gameboard._board[y_to - 2][x_to]).get_name() != "Empty":  # Intervening piece
                    return False
                else:
                    return True

    def check_horse_move(self, from_x, from_y, to_x, to_y, current_piece, move_to_piece):
        """Check whether move is valid for horse"""
        if (to_y - from_y) == 2: # Up
            if (self._gameboard._board[from_y][from_x - 1]).get_name() == "Empty":
                if (to_x - from_x) == 1 or (from_x - to_x) == 1:
                    return True
                else:
                    return False
            else:
                return False
        elif (from_y - to_y) == 2: # Down
            if (self._gameboard._board[from_y - 2][from_x - 1]).get_name() == "Empty":
                if (to_x - from_x) == 1 or (from_x - to_x) == 1:
                    return True
                else:
                    return False
            else:
                return False
        elif (to_x - from_x) == 2: # Left
            if (self._gameboard._board[from_y - 1][from_x]).get_name() == "Empty":
                if (to_y - from_y) == 1 or (from_y - to_y) == 1:
                    return True
                else:
                    return False
            else:
                return False
        elif (from_x - to_x) == 2: # Right
            if (self._gameboard._board[from_y - 1][from_x - 2]).get_name() == "Empty":
                if (to_y - from_y) == 1 or (from_y - to_y) == 1:
                    return True
                else:
                    return False
            else:
                return False

class GameEngine:
    """Represents game engine for Xiangqi"""
    def __init__(self):
        self.game = XiangqiGame()

    def engine(self):
        """Game engine for Xiangqi"""
        play_game = "yes"
        while play_game == "yes":
            self.game.get_game_board().print_board()
            print("Red goes first.")
            while self.game.get_game_state() == "UNFINISHED":
                try:
                    user_move_from = input("Enter the position of the piece you'd like to move in algebraic notation: ")
                    user_move_to = input("Enter the position you'd like to move the piece to: ")
                    self.game.make_move(user_move_from, user_move_to)
                    self.game.get_game_board().print_board()
                except ValueError:
                    print("This is not valid notation. Please try again.")
                    continue
            play_again = input("Would you like to play again: ")
            play_game = play_again.lower()



### Instantiation game for testing ###
def main():
    game = GameEngine()
    game.engine()

if __name__ == '__main__':
    main()

