from state import State



''' 
    Class that captures N_queens problem takes a size parameter and creates an intial state tuple with None values 
    implementation derivations for some class methods credit goes to https://github.com/aimacode/aima-python/blob/master/search.py
'''
class N_Queens:

    def __init__(self, n_size):
      self.n_size = n_size
      self.total_size = pow(self.n_size, 2)
      self.start_state = State(tuple([None] * n_size), None, 0, 0)

    
    ''' Computes succession of states from previous state '''
    def compute_successors(self, node):
        print(self.get_moves(node), node.state)
        return [ State(self.place_queen(node, move), node, node.depth + 1, node.cost + 1) for move in self.get_moves(node) ]

    
    ''' gets array of available rows per column '''
    def get_moves(self, node):
        col = self.get_empty_column(node.state)

        #check if all queens have been placed
        if self.all_queens_placed(node.state):
            return list() 
        else: 
            return [ row for row in range(self.n_size) if not self.clashes(node.state, row, col) ]

    ''' Gets next empty column '''
    def get_empty_column(self, state):
        return state.index(None)
    
    ''' determines if all queens have been placed '''
    def all_queens_placed(self, state):
        return state[-1] != None

    ''' determines if there are any clashes when placing a queen on the column '''
    def clashes(self, state, row, column):

        return any(self.clash(row, column, state[idx], idx) for idx in range(column))


    """ checks for a single clash between placing two queens in (row1, col1) and (row2, col2) """
    def clash(self, row_1, column_1, row_2, column_2):
        return (row_1 == row_2 or
                column_1 == column_2 or  
                row_1 - column_1 == row_2 - column_2 or  
                row_1 + column_1 == row_2 + column_2)
    
    """ places a queen in a row of the board """
    def place_queen(self, node, queen):
        column = self.get_empty_column(node.state)
        new_state = list(node.state)
        new_state[column] = queen
        print('new state', new_state)
        return tuple(new_state)

    """Check if all queens are placed w/o conflicts."""
    def is_goal(self, state):
        if not self.all_queens_placed(state):
            return False
        return not any(self.clashes(state, state[col], col)
                for col in range(len(state)))                   

    def __str__(self):
        print(str(self.goal_state))