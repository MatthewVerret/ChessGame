import Board
from tkinter import N
import Enum_Pieces

"""
    _summary_: This class
"""


class Board_Creation():
    board_game: list[list] = [None]*8

    # rook / bishop / knight / queen / king /...
    pieces_white = ['R', 'B', 'K', 'Q', 'O', 'K', 'B', 'R']
    pawns = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
    pieces_black = ['R', 'B', 'K', 'O', 'Q', 'K', 'B', 'R']
    row_even = ['.', ' ', '.', ' ', '.', ' ', '.', ' ', ]
    row_odd = [' ', '.', ' ', '.', ' ', '.', ' ', '.']

    # Position
    pos: str = "     a   b   c   d   e   f   g   h"

    def asg_tuple_piece(self) -> None:
        for row in range(len(self.board_game)):
            if row == 0:
                self.board_game[row] = self.pieces_white
                continue
            if row == 1 or row == 6:
                self.board_game[row] = self.pawns
                continue
            if row == 7:
                self.board_game[row] = self.pieces_black
                continue
            else:
                if row % 2:
                    self.board_game[row] = self.row_even
                else:
                    self.board_game[row] = self.row_odd

    # working
    # Show the board created
    def showBoardPieces(self) -> None:
        self.asg_tuple_piece(self)
        board: str = ""
        board += ' ' * 15 + "~~WHITE~~\n"
        board += self.pos + '\n'
        for row in range(len(self.board_game)):
            board += f"{9-row-1}  |"
            for position_in_row in range(len(self.board_game)):
                board += f" {self.board_game[row][position_in_row]} |"
            board += f"  {9-row-1} \n"
        board += self.pos + '\n'
        board += ' ' * 15 + "~~BLACK~~"
        print(board)
