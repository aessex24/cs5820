import math
from collections import deque
from queue import LifoQueue
from state import State

failure = State('failure', None, math.inf, math.inf)
cutoff  = State('cutoff', None, math.inf, math.inf)

''' implementation of breadth first search '''
def bfs(initial, goal, expander):
    visited, queue = set(), deque([initial])

    while queue:

        node = queue.popleft()

        if goal(node.state):
            print('Found Answer')
            return node

        for neighbor in expander(node):
            if neighbor.state not in visited:
                queue.append(neighbor)
                visited.add(neighbor.state)
    return failure

''' implementation of depth first search '''
def dfs(initial, goal, expander):
    visited, stack = set(), list([initial])
    
    while stack:

        node = stack.pop()


        if goal(node.state):
            return node

        visited.add(node.state)

        # print(len(stack))
  
        for child in reversed(expander(node)):
            if child.state not in visited:
                stack.append(child)
    return failure

''' implementation fo iterative deepening search '''
def ids(initial, goal, expander):
    limit = 12
    depth = 0
    result = None

    while result == None:
        if depth >= limit:
            result = cutoff
        else:
            result = depth_limited(initial, goal, expander, depth)
        depth +=1
    return result

''' implementation of depth limited portion of id '''
def depth_limited(initial, goal, expander, depth):
    queue = LifoQueue()
    queue.put(initial)
    
    while True:
        #print(depth, queue.qsize())
        if queue.empty():
            return None
        current = queue.get()
        if goal(current.state):
            return current
        elif current.depth is not depth:
            for successor in expander(current):
                queue.put(successor)


''' implementation of bidirectional '''
def bd(initial, dest, expander):

    #create src and dest queues along with visited lookup tables
    src_explored, src_stack = set(), list([initial])
    dest_explored, dest_stack = set(), list([dest])


    while src_stack and dest_stack:

        front_node = src_stack.pop(0)
        back_node = dest_stack.pop(0)


        src_explored.add(front_node.state)
        dest_explored.add(back_node.state)

        if front_node.state in dest_explored and back_node.state in src_explored:
            return front_node or back_node

        # expand in forward direction
        neighbors_1 = expander(front_node)
        for neighbor in neighbors_1:
            if neighbor.state not in src_explored:
                src_stack.append(neighbor)
                src_explored.add(neighbor.state)

        #expand in backward direction
        neighbors_2 = expander(back_node)
        for neighbor in neighbors_2:
            if neighbor.state not in dest_explored:
                dest_stack.append(neighbor)
                dest_explored.add(neighbor.state)
    return failure