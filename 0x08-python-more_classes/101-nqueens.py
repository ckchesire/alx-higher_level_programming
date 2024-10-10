#!/usr/bin/python3
import sys
"""This module solves the N queens puzzle of placing N non-attacking
    queens on an NxN chessboard.
"""


class NQueens:
    """Encapsulates the data and functionalilty used in solving the
        N queens problem.
    """
    def __init__(self, N):
        """Initialize the board values

            Args:
             N (int): size of the board
             board (int): initializes 2D board having x and y axis
        """
        self.N = N
        self.board = [[0 for x in range(N)] for y in range(N)]

    def print_sln(self):
        """Prints solution to N queens problem
        """
        sln = []
        for row in range(self.N):
            for col in range(self.N):
                if self.board[row][col] == 1:
                    sln.append([row, col])
        print(sln)

    def is_safe(self, row, col):
        """Function checks whether it is safe to place a queen at a
            position.

            Args:
                row (int): row on the board
                col (int): column on the board

            Return:
                Returns 'False' if there is conflict and 'True' if safe.
        """
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_problem(self, col=0):
        """Function attempts to solve the N queens problem using backtracking

            Args:
                col (int): column on the board

            Return:
                returns 'True' if solution found otherwise 'False'
        """
        if col >= self.N:
            self.print_sln()
            return True

        found_sln = False
        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                found_sln = self.solve_problem(col + 1) or found_sln
                self.board[i][col] = 0

        return found_sln

    @staticmethod
    def validate_input(args):
        """ Static method handles the validation of input arguments
            passed from the command line

            Args:
                args(int) : command line argument count

            Returns:
                returns size of board N
        """
        if len(args) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            N = int(args[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        return N


if __name__ == "__main__":
    N = NQueens.validate_input(sys.argv)
    nqueens = NQueens(N)
    if not nqueens.solve_problem():
        print("No solution exists")
