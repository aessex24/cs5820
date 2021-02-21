import timeit
import argparse

from queens import N_Queens
from search import bfs, dfs, ids

nsize = 4
tsize = pow(nsize, 2)

search_map = {
  'bfs': bfs,
  'dfs': dfs,
  'ids': ids,
}


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


  start = timeit.default_timer()

  frontier = search_function(board.start_state, board.is_goal, board.compute_successors)

  stop = timeit.default_timer()
  
  print('answer', frontier)

  print(f'\nTime Taken')
  print(10 * '-')
  print(f'{stop-start}')


if __name__ == '__main__':
  main()    

