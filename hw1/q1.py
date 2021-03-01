import timeit
import argparse

from puzzle import N_Puzzle
from search import bfs, dfs, ids, bd

nsize = 5
tsize = pow(nsize, 2)

search_dictionary = {
  'bfs': bfs,
  'dfs': dfs,
  'ids': ids,
  'bd': bd,
  'all': None
}

def print_state(node):
    for (index, value) in enumerate(node):
        print(' %s ' % value, end=' ') 
        if index in [x for x in range(nsize - 1, tsize, nsize)]:
            print() 
    print() 

def compare_searches(initial_state, is_goal, goal_state, expander):

  # time bfs
  start_bfs = timeit.default_timer()
  bfs_frontier = bfs(initial_state, is_goal, expander)
  stop_bfs = timeit.default_timer()

  # time dfs
  start_dfs = timeit.default_timer()
  dfs_frontier = dfs(initial_state, is_goal, expander)
  stop_dfs = timeit.default_timer()

  # time ids
  start_ids = timeit.default_timer()
  ids_frontier = ids(initial_state, is_goal, expander)
  stop_ids = timeit.default_timer()
  
  # time bd
  start_bd = timeit.default_timer()
  bd_frontier = bd(initial_state, goal_state, expander)
  stop_bd = timeit.default_timer()

  print(f'\nTime Taken')
  print(10 * '-')
  print(f'Breadth first: {stop_bfs-start_bfs}', bfs_frontier)
  print(f'Depth first: {stop_dfs-start_dfs}', dfs_frontier)
  print(f'iterative deepening: {stop_ids-start_ids}', ids_frontier)
  print(f'Bidirectional: {stop_bd-start_bd}', bd_frontier)




def main():

  # parse cli arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('algorithm')
  args = parser.parse_args()

  #select search function
  search_function = search_dictionary[args.algorithm]

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



  if(args.algorithm == 'all'):
    compare_searches(initial_state, puzzle.is_goal, goal_state, puzzle.compute_successors)
    return

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

