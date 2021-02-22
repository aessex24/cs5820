import timeit
import argparse

from queens import N_Queens
from search import bfs, dfs, ids, bd

nsize = 10
tsize = pow(nsize, 2)

search_map = {
  'bfs': bfs,
  'dfs': dfs,
  'ids': ids,
  'bd' : bd,
  'all': all
}

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
  # start_bd = timeit.default_timer()
  # bd_frontier = bd(initial_state, goal_state, expander)
  # stop_bd = timeit.default_timer()

  print(f'\nTime Taken')
  print(10 * '-')
  print(f'Breadth first: {stop_bfs-start_bfs}', bfs_frontier)
  print(f'Depth first: {stop_dfs-start_dfs}', dfs_frontier)
  print(f'iterative deepening: {stop_ids-start_ids}', ids_frontier)
  # print(f'Bidirectional: {stop_bd-start_bd}', bd_frontier)

goal_state = (2, 0, 3, 1)
def main():

  # parse cli arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('algorithm')
  args = parser.parse_args()

  #select search function
  search_function = search_map[args.algorithm]

  # Initialize puzzle
  print('N-Queen Solver!')
  print(10 * '-')
  board = N_Queens(nsize)

  # generate psuedo random start state
  print('The Starting State is:')
  print(board.start_state, '\n')
  
  if(args.algorithm == 'all'):
    compare_searches(board.start_state, board.is_goal,board.create_goal_state(goal_state), board.compute_successors)
    return

  start = timeit.default_timer()

  if(args.algorithm == 'bd'):
    frontier = search_function(board.start_state, board.create_goal_state(goal_state), board.compute_successors)
  else:
    frontier = search_function(board.start_state, board.is_goal, board.compute_successors)

  stop = timeit.default_timer()
  
  print('answer', frontier)

  print(f'\nTime Taken')
  print(10 * '-')
  print(f'{stop-start}')


if __name__ == '__main__':
  main()    

