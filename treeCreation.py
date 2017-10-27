# TODO link to nPuzzle.py
import heapq

class TreeCreation: # TODO: LOOK UP AND SEE IF THERE SHOULD BE AN __init__ METHOD
    # TODO: CHECK IF VARIABLES NEED TO BE INITIALIZED
    # TODO: AND BY EXTENSION, WHAT "self" MEANS? (ex. self.puzzle, self.zero_position, etc)
    # TODO: ALSO THE HASH TABLE OF REPEATED STATES
    repeatedStates = dict()

    def __init__(self, puzzle):
        created_tree = 0 # TODO: IMPLEMENT
        # currently initialized as 0; needs to be an actual tree -- not sure if the tree...
        # ...should be made here in the constructor,
        # or if it should be in a separate function, like commented below

        return created_tree

    #def create_tree(puzzle):
    #    tree = 0  # TODO: IMPLEMENT
    #    # currently an int; needs to be an actual tree; this is just a skeleton
    #    return tree

    def tree_traversal(self, cost):
        cost = cost + 1 # TODO: IMPLEMENT
        # it only costs 1 if it's uniform cost search; tree traversal in general needs to...
        # ... handle the other two heuristics
        # TODO: ADD NODE TO THE HASH TABLE

        return cost