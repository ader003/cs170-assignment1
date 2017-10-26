#import heapq

#the different choices in puzzles offered/test cases
trivial = [1, 2, 3,
           4, 5, 6,
           7, 8, 0]
veryEasy = [1, 2, 3,
            4, 5, 6,
            7, 0, 8]
easy = [1, 2, 0,
        4, 5, 3,
        7, 8, 6]
doable = [0, 1, 2,
          4, 5, 3,
          7, 8, 6]
ohBoy = [8, 7, 1,
         6, 0, 2,
         5, 4, 3]
impossible = [1, 2, 3,
              4, 5, 6,
              8, 7, 0]

userPuzzle = [] #placeholder


def main():
    puzzleMode = raw_input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.")
    if puzzleMode == 1:
        puzzleSelected = defaultPuzzleMode()
        printPuzzle(puzzleSelected)

    if puzzleMode == 2:
        print "Enter your puzzle, using a zero to represent the blank. +" \
              "Enter each row using a space or tab between each number."
        #how to translate the above format into an array


def defaultPuzzleMode():
    defaultDifficulty = raw_input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5.")
    if defaultDifficulty == 0:
        print "Difficulty of 'Trivial' selected."
        return trivial
    if defaultDifficulty == 1:
        print "Difficulty of 'Very Easy' selected."
        return veryEasy
    if defaultDifficulty == 2:
        print "Difficulty of 'Easy' selected."
        return easy
    if defaultDifficulty == 3:
        print "Difficulty of 'Doable' selected."
        return doable
    if defaultDifficulty == 4:
        print "Difficulty of 'Oh Boy' selected."
        return ohBoy
    if defaultDifficulty == 5:
        print "Difficulty of 'Impossible' selected."
        return impossible


def printPuzzle(puzzle):
    print puzzle.at(0) + " " + puzzle.at(1) + puzzle.at(2) + '\n' + \
          puzzle.at(3) + " " + puzzle.at(4) + " " + puzzle.at(5) + '\n' + \
          puzzle.at(6) + " " + puzzle.at(7) + " " + puzzle.at(8) + '\n'

if __name__ == '__main__':
    main()


