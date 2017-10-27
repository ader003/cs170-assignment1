#import heapq

#the different choices in puzzles offered/test cases
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]
easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]
doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]
ohBoy = [[8, 7, 1],
         [6, 0, 2],
         [5, 4, 3]]
impossible = [[1, 2, 3],
              [4, 5, 6],
              [8, 7, 0]]
userPuzzle_string = " "
goalState = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]


def main():
    puzzleMode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own."
                       + '\n')
    if puzzleMode == "1":
        printPuzzle(defaultPuzzleMode())

    if puzzleMode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
              "Enter each row using a space or tab between each number. RET only when finished." + '\n')
        input(userPuzzle_string)
        userPuzzle = [x for x in userPuzzle_string in userPuzzle_string]
        print(userPuzzle) #TODO: delete; temporary for for testing purposes

#        for i in range(0, 2):
#            for j in range(0, 2):
#                puzzleString = input(userPuzzle.at(i, j))
#                userPuzzle = puzzleString.str()
    return



def defaultPuzzleMode():
    selectedDifficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    if selectedDifficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selectedDifficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selectedDifficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selectedDifficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selectedDifficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        return ohBoy
    if selectedDifficulty == "5":
        print("Difficulty of 'Impossible' selected.")
        return impossible


def printPuzzle(puzzle):
    for i in range(0, 3):
        print(puzzle[i])

if __name__ == '__main__':
    main()


