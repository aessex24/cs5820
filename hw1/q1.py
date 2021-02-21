import timeit
import argparse

from puzzle import N_Puzzle
from search import bfs, dfs, ids, bd

nsize = 4
tsize = pow(nsize, 2)

function_map = {
  'bfs': bfs,
  'dfs': dfs,
  'ids': ids,
  'bd': bd
}

def print_state(node):
    """Print the list in a Matrix Format."""

    for (index, value) in enumerate(node):
        print(' %s ' % value, end=' ') 
        if index in [x for x in range(nsize - 1, tsize, nsize)]:
            print() 
    print() 

def main():

  # parse cli arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('algorithm')
  args = parser.parse_args()

  #select search function
  search_function = function_map[args.algorithm]

  # Initialize puzzle
  print('N-Puzzle Solver!')
  print(10 * '-')
  puzzle = N_Puzzle(nsize)

  # generate psuedo random start state
  initial_state = puzzle.generate_start_state()
  print('The Starting State is:')
  print_state(initial_state.state)

  # generate goal state
  goal_state = puzzle.generate_goal_state()
  print('The Goal State is be:')
  print_state(goal_state.state)


  start = timeit.default_timer()

  if(args.algorithm == 'bd'):
    frontier = search_function(initial_state, goal_state, puzzle.compute_successors)
  else:
    frontier = search_function(initial_state, puzzle.is_goal, puzzle.compute_successors)


  stop = timeit.default_timer()
  
  print('answer', frontier)

  print(f'\nTime Taken')
  print(10 * '-')
  print(f'{stop-start}')


if __name__ == '__main__':
  main()    

