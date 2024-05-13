#!/usr/bin/python3
"""Module with a python script"""
from sys import argv, exit


def find_queen_positions(
        board_size, row_index=0,
        col_placement=[], up_diagonal=[], down_diagonal=[]):
    """Function that finds possible queen positions"""
    if row_index < board_size:
        for col_index in range(board_size):
            if col_index not in col_placement and \
                    row_index + col_index not in up_diagonal and \
                    row_index - col_index not in down_diagonal:
                yield from find_queen_positions(
                        board_size, row_index + 1,
                        col_placement + [col_index],
                        up_diagonal + [row_index + col_index],
                        down_diagonal + [row_index - col_index])
    else:
        yield col_placement


def solve_n_queens(board_size):
    """Function that solves the N queens problem"""
    queen_positions = []
    row_index = 0
    for solution in find_queen_positions(board_size, 0):
        for col_index in solution:
            queen_positions.append([row_index, col_index])
            row_index += 1
        print(queen_positions)
        queen_positions = []
        row_index = 0


if __name__ == "__main__":
    if not 1 < len(argv) < 3:
        print("Usage: nqueens N")
        exit(1)

    try:
        board_size = int(argv[1])
        if board_size < 4:
            print("N must be at least 4")
            exit(1)
        solve_n_queens(board_size)

    except Exception as _:
        print("N must be a number")
        exit(1)
