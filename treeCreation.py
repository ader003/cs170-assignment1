# TODO link to nPuzzle.py
import heapq

class TreeCreation: # TODO: LOOK UP AND SEE IF THERE SHOULD BE AN __init__ METHOD
    # TODO: CHECK IF VARIABLES NEED TO BE INITIALIZED
    # TODO: AND BY EXTENSION, WHAT "self" MEANS? (ex. self.puzzle, self.zero_position, etc)
    def __init__(self, puzzle):
        created_tree = 0 # TODO: IMPLEMENT
        # currently initialized as 0; needs to be an actual tree -- not sure if the tree should be made here in the constructor,
        # or if it should be in a separate function, like commented below

        return created_tree

    #def create_tree(puzzle):
    #    tree = 0  # TODO: IMPLEMENT
    #    # currently an int; needs to be an actual tree; this is just a skeleton
    #    return tree

    def updated_puzzle(puzzle): # for the puzzle tracing
        # TODO: IMPLEMENT
        for i in range(0, 3):
            print(puzzle[i])