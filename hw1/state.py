class State:

    def __init__(self, state, parent, depth, cost):

        self.state = state

        self.parent = parent

        self.depth = depth

        self.cost = cost

    def __str__(self):  
        return f' state: {self.state}, depth: {self.depth}, cost: {self.cost}'
