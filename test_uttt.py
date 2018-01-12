"""Unit tests for Ultimate Tic Tac Toe (uttt.py)

Run this file to run the unit tests.
"""

import unittest
import uttt


class TestCase(unittest.TestCase):

    def test_board_creation(self):
        b = uttt.Board()
        b.make_move(0, 2)

    def test_board_reset(self):
        b = uttt.Board()
        b.make_move(0, 4)
        self.assertEqual(b.move_count(), 1)
        b.reset()
        self.assertEqual(b.move_count(), 0)

    def test_illegal_move(self):
        """
        Does a test on the possible illegal board moves.
        """
        b = uttt.Board()
        b.make_move(1, 3)
        # The next move has to be in cell 3.
        self.assertRaises(uttt.IllegalMoveError, b.make_move, 4, 2)
        # Out of board move.
        self.assertRaises(ValueError, b.make_move, -1, 2)
        # Out of board move.
        self.assertRaises(ValueError, b.make_move, 3, 9)

    def test_duplicate_move(self):
        """
        Tests to make sure a duplicate move throws an exception.
        """
        b = uttt.Board()
        b.make_move(1, 3)
        b.make_move(3, 1)
        self.assertRaises(uttt.IllegalMoveError, b.make_move, 1, 3)

    def test_winning_cell(self):
        b = uttt.Board()
        b.make_move(1, 3)
        b.make_move(3, 2)
        b.make_move(2, 4)
        b.make_move(4, 0)
        b.make_move(0, 8)
        b.make_move(8, 6)
        b.make_move(6, 0)
        b.make_move(0, 0)
        b.make_move(0, 2)
        b.make_move(2, 1)
        b.make_move(1, 0)
        b.make_move(0, 4)
        b.make_move(4, 3)
        b.make_move(3, 1)
        b.make_move(1, 6)
        self.assertEqual(b.move_count(), 15)
        self.assertFalse(b.is_game_over())
        self.assertEqual(b.get_cell_winner(1), 'X')
        b.make_move(6, 4)
        b.make_move(4, 4)
        b.make_move(4, 1)
        b.make_move(1, 5)
        b.make_move(5, 3)
        b.make_move(3, 3)
        b.make_move(3, 4)
        b.make_move(4, 5)
        # Middle cell should be won hy X now.
        self.assertEqual(b.get_cell_winner(4), 'X')
        b.make_move(5, 7)
        b.make_move(7, 4)
        b.make_move(4, 7)
        b.make_move(7, 1)
        b.make_move(1, 7)
        b.make_move(7, 7)
        self.assertEqual(b.get_cell_winner(7), 'X')
        self.assertTrue(b.is_game_over())
        self.assertEqual(b.get_winner(), 'X')


if __name__ == '__main__':
    unittest.main()
