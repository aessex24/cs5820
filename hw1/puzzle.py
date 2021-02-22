import random
from state import State

''' 
    Class that captures N_Puzzle problem takes a size parameter and creates a goal state tuple 
    implementation derivations for some class methods credit goes to https://github.com/aimacode/aima-python/blob/master/search.py
'''
class N_Puzzle:

    def __init__(self, n_size):
      self.n_size = n_size
      self.total_size = pow(self.n_size, 2)
      self.goal_state = list(range(1, self.total_size))
      self.goal_state.append(0)
      self.goal_state = tuple(self.goal_state)
      self.possible_moves = [1, -1, self.n_size, -self.n_size] # right, left, up, and down

    

    '''
        Function returns possible legal moves for each tile position
    '''
    def get_moves(self, tile):
        all_moves = [ self.get_move(tile, move) for move in self.possible_moves ]
        return [ x for x in all_moves if x is not None ]
        
        # values = [1, -1, self.n_size, -self.n_size]
        # valid = []
        # for x in values:
        #     if 0 <= tile + x < self.total_size:
        #         if x == 1 and tile in range(self.n_size - 1, self.total_size, 
        #                 self.n_size):
        #             continue
        #         if x == -1 and tile in range(0, self.total_size, self.n_size):
        #             continue
        #         valid.append(x)
        # return valid 

    def get_move(self, tile, move):
        if 0 <= tile + move < self.total_size:
            if move == 1 and tile in range(self.n_size - 1, self.total_size, self.n_size):
                return None
            if move == -1 and tile in range(0, self.total_size, self.n_size):
                return None
            return move

    ''' Computes succession of states from previous state '''
    def compute_successors(self, node):
        # get valid moves for each tile
        expanded_states_dict = { key:self.get_moves(key) for key in range(self.total_size) } 

        # get index for tile 0
        pos = self.get_blank_tile(node.state)

        # extract legal moves from dictionary
        moves = expanded_states_dict[pos]

        # loop through moves and switches postions creating new states for each move
        return [ State(self.move_tile(node.state, mv, pos), node, node.depth + 1, node.cost + 1) for mv in moves ]


    ''' moves the 0 tile up, down, left, or right '''
    def move_tile(self, state, mv, pos):
        new_state = list(state)
        (new_state[pos + mv], new_state[pos]) = (new_state[pos], new_state[pos + mv])
        return tuple(new_state)

    ''' return index of blank tile (0) '''
    def get_blank_tile(self, state):
        return state.index(0)

    ''' Generates a psudeo random start state just returning a list '''
    def compute_start_state(self, curr_state):
        
        # get valid moves for each tile
        expanded_states_dict = { key:self.get_moves(key) for key in range(self.total_size) } 

        pos = self.get_blank_tile(curr_state)

        moves = expanded_states_dict[pos]
        
        return [ self.move_tile(curr_state, mv, pos) for mv in moves ]

    ''' Select a random state '''
    def one_of_poss(self, curr_state):
        return random.choice(self.compute_start_state(curr_state))

    ''' generate a psudeo random start state '''
    def generate_start_state(self, seed=50):
        start_state = self.goal_state[:]
        for _ in range(seed):
            start_state = self.one_of_poss(start_state)
        return State(tuple(start_state), None, 0, 0)
    
    ''' checks if goal state is found '''
    def is_goal(self, state):
        return state == self.goal_state
    
    ''' returns state object from goal state '''
    def generate_goal_state(self):
        return State(tuple(self.goal_state), None, 0, 0)

    def __str__(self):
        print(str(self.goal_state))