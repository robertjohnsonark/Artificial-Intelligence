from sudoku import Sudoku
from copy import deepcopy
import numpy as np



class CSP_Solver(object):
    """
    This class is used to solve the CSP with backtracking using the minimum value remaining heuristic.
    HINT: you will likely want to implement functions in the backtracking sudo code in figure 6.5 in the text book.
            We have provided some prototypes that might be helpful. You are not required to use any functions defined
            here and can modify any function other than the solve method. We will test your code with the solve method
            and so it must have no parameters and return the type it says. 
         
    """
    def __init__(self, puzzle_file):
        '''
        Initialize the solver instance. The lower the number of the puzzle file the easier it is. 
        It is a good idea to start with the easy puzzles and verify that your solution is correct manually. 
        You should run on the hard puzzles to make sure you aren't violating corner cases that come up.
        Harder puzzles will take longer to solve.
        :param puzzle_file: the puzzle file to solve 
        '''
        self.sudoku = Sudoku(puzzle_file) # this line has to be here to initialize the puzzle
        # print ("Sudoku", Sudoku.board_str(self.sudoku))
        # print("board", self.sudoku.board) - List of Lists 
        self.num_guesses = 0
        # self.unassigned = deque()
        self.assignment = {}
        
        # make domian the Given Puzzle
        self.domains = deepcopy(self.sudoku.board)
        # Overwrite 0's with their possiblilities.
        for row in range(0,9):
            for col in range(0,9):
                # extract value
                value = self.sudoku.board[row][col]
                if value == 0:
                    self.domains[row][col] = [1,2,3,4,5,6,7,8,9]
                    # add this index to unassigned for faster look ups
                    # self.unassigned.append((row,col))
                else: 
                    self.domains[row][col] = value
                    self.assignment[(row, col)] = value

        vars=[]
        # self.csp = CSP(vars, self.domains)

    ################################################################
    ### YOU MUST EDIT THIS FUNCTION!!!!!
    ### We will test your code by constructing a csp_solver instance
    ### e.g.,
    ### csp_solver = CSP_Solver('puz-001.txt')
    ### solved_board, num_guesses = csp_solver.solve()
    ### so your `solve' method must return these two items.
    ################################################################
    def solve(self):
        '''
        This method solves the puzzle initialized in self.sudoku 
        You should define backtracking search methods that this function calls
        The return from this function NEEDS to match the correct type
        Return None, number of guesses no solution is found
        :return: tuple (list of list (ie [[]]), number of guesses
        '''
        for row in range(9):
            for col in range(9):
                if self.sudoku.board[row][col] == 0:
                    for n in range(1, 10):
                        if self.verify(row, col, n):
                            self.sudoku.board[row][col] = n
                            self.solve()
                            self.num_guesses += 1
                            self.sudoku.board[row][col] = 0
                    return self.sudoku.board, self.num_guesses
        # self.backtracking_search()
        print ("board", self.sudoku.board)
        print("num", self.num_guesses)

    def backtracking_search(self):
        '''
        This function might be helpful to initialize a recursive backtracking search function
        You do not have to use it.

        :param sudoku: Sudoku class instance
        :param csp: CSP class instance
        :return: board state (list of lists), num guesses
        '''

        return self.recursive_backtracking(self.assignment)

    def verify(self, row, col, n):
        for i in range(9):
            if self.sudoku.board[row][i] == n:
                return False

        for i in range(9):
            if self.sudoku.board[i][col] == n:
                return False

        row0 = (row // 3) * 3
        col0 = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.sudoku.board[row0 + i][col0 + j] == n:
                    return False

        return True

    def recursive_backtracking(self, assignment):
        '''
        recursive backtracking search function.
        You do not have to use this
        :param sudoku: Sudoku class instance
        :param csp: CSP class instance
        :return: board state (list of lists)
        '''
        # return a solution or failure
        # if assignment is complete then return the assignment

        return None


if __name__ == '__main__':
    csp_solver = CSP_Solver('puz-001.txt')
    solution, guesses = csp_solver.solve()

