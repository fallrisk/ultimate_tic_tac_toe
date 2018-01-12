"""Ultimate Tic Tac Toe
"""
__author__ = 'Justin Watson'


class IllegalMoveError(Exception):
    pass


class Board(object):
    """
    Representation of an Ultimate Tic-Tac-Toe board. Player X always
    goes first.

    0 | 1 | 2
    ----------
    3 | 4 | 5
    ----------
    6 | 7 | 8

    This is the representation of the main board. Within each cell of the main
    board is another board with the same numbering as the main board.
    """

    """List of possible ways to win."""
    _winning_combos = [
        (0, 1, 2),
        (0, 3, 6),
        (0, 4, 8),
        (3, 4, 5),
        (6, 7, 8),
        (1, 4, 7),
        (2, 5, 8),
        (2, 4, 6)
    ]

    """A list of all the moves made."""
    _moves = []

    """The move we are on."""
    _move_number = 0

    """Settings """
    _board = [['E' for sc in range(9)] for c in range(9)]

    """Winner of the game. 'N' means no winner. 'X' means player X won, and
    'O' means player 'O' won. """
    _winner = 'N'

    def __init__(self):
        self.reset()

    def reset(self):
        """
        Resets the board.
        """
        self._board = [['E' for sc in range(9)] for c in range(9)]
        self._move_number = 0
        self._winner = 'N'
        self._moves = []

    def make_move(self, cell, subcell):
        """
        Make a board move.

        @param cell The cells start from top left as 0. Here is what
        it looks like.

        0 | 1 | 2
        ----------
        3 | 4 | 5
        ----------
        6 | 7 | 8

        @param subcell The sub cell is the cell within cell specified above.
        @param mark Mark can be either X or O.
        @throw Throws an IllegalMoveError if the move can't be done.
        @throw Throws a ValueError if the cell or subcell is not valid.
        """
        if 0 > cell or cell > 8:
            raise ValueError
        if 0 > subcell or subcell > 8:
            raise ValueError
        # Check to make sure the move is in the cell that the previous subcell
        # was marked.
        if self._move_number > 0:
            previous_move = self._moves[len(self._moves) - 1]
            if cell is not previous_move[1]:
                raise IllegalMoveError
            # Check for duplicate move.
            if self.get_mark(cell, subcell) is not 'E':
                raise IllegalMoveError
        mark = 'X' if (self._move_number % 2 == 0) else 'O'
        self._board[cell][subcell] = mark
        self._moves.append((cell, subcell, mark))
        self._move_number = self._move_number + 1

    def _is_board_won(self, board):
        """
        Checks to see if a board has been won by a player. A board is
        represented as a list as defined in the class definition. Not
        this class but the subpart of it.
        """
        b = board
        # Check to make sure that the cells are not empty, and then check
        # to see if they are all equal. If the are all equal then someone
        # won that board.
        for p in self._winning_combos:
            if b[p[0]] == 'E' or b[p[1]] == 'E' or b[p[2]] == 'E':
                continue
            if b[p[0]] == 'N' or b[p[1]] == 'N' or b[p[2]] == 'N':
                continue
            if b[p[0]] == b[p[1]] and b[p[1]] == b[p[2]]:
                return b[p[0]]
        return 'N'

    def get_cell_winner(self, cell):
        """
        @param cell The board within the board to check.
        @return Retruns 'X' if X won the cell or 'O' if player O won the cell.
            Can also return 'N' if no one won the subcell or 'T' for a tie.
        """
        return self._is_board_won(self._board[cell])

    def is_game_over(self):
        """
        The game is over if a player has 3 in a row in the cell (root). The
        game is also over if the game is a draw (tie).
        """
        # Generate a list of the winners of the subboards and check to see if
        # someone won the overall board.
        b = []
        for x in range(9):
            b.append(self._is_board_won(self._board[x]))
        r = self._is_board_won(b)
        if r == 'X' or r == 'O':
            self._winner = r
            return True
        else:
            return False

    def move_count(self):
        """
        @return Returns the current move number you are on.
        """
        return self._move_number

    def get_winner(self):
        """
        Returns the winner of the game, if there is one.
        @return Returns 'N' for no winner. 'X' for player X, and 'O' for
        player O.
        """
        return self._winner

    def get_mark(self, cell, subcell):
        """ Returns the mark at the subcell of
        the board. Cell is the top layer, and subcell is the cell within the
        cell of the top layer board. @return Returns 'E' for empty. 'X' for
        player X, and 'O' for player O. """
        return self._board[cell][subcell]

    def get_moves(self):
        return self._moves

    def __str__(self):
        s = ''
        for b in range(9):
            for sb in range(9):
                s = s + ' ' + self._board[b][sb]
            s = s + '\n'
        return s
