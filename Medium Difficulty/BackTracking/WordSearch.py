class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        alreadyUsed = self.getVisitedArray(board)

        first_letter = word[0]

        occurences = set()

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == first_letter:
                    occurences.add((i,j))

        if len(word) == 1 and len(occurences) > 0:
            return True

        for occ in occurences:
            if self.FindLetterFollwingPAthWay(occ[0],occ[1],word,self.getVisitedArray(board),board):
                return True

        return False


    def getVisitedArray(self, grid):
        visited = dict()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                visited[(i, j)] = False
        return visited

    def FindLetterFollwingPAthWay(self, i, j, word_left, alreadyVisitedInPathWay, grid):
        if len(word_left) == 1:
            if grid[i][j] == word_left[0]:
                return True

        if grid[i][j] != word_left[0]:
            return False

        adjacents_cells = self.getAdjCoordinates(i, j, len(grid), len(grid[0]))
        for cell in adjacents_cells:
            if not alreadyVisitedInPathWay[cell]:
                temp_visited = alreadyVisitedInPathWay
                temp_visited[(i, j)] = True
                if self.FindLetterFollwingPAthWay(cell[0], cell[1], word_left[1:], temp_visited, grid):
                    return True
                temp_visited[(i,j)] = False
        return False

    def getAdjCoordinates(self, i, j, n_lig, n_col):
        coordinates = []
        if n_col == 1 and n_lig == 1:
            return coordinates
        elif n_lig == 1:
            if j == 0:
                coordinates.append((i, j + 1))
            elif j == n_col - 1:
                coordinates.append((i, j - 1))

            else:
                coordinates.append((i, j + 1))
                coordinates.append((i, j - 1))

        elif n_col == 1:
            if i == 0:
                coordinates.append((i + 1, j))
            elif i == n_lig - 1:
                coordinates.append((i - 1, j))
            else:
                coordinates.append((i + 1, j))
                coordinates.append((i - 1, j))


        elif i == 0 and j == 0:
            coordinates.append((i, j + 1))
            coordinates.append((i + 1, j))
        elif i == 0 and j == n_col - 1:
            coordinates.append((i, j - 1))
            coordinates.append((i + 1, j))
        elif i == n_lig - 1 and j == 0:
            coordinates.append((i, j + 1))
            coordinates.append((i - 1, j))
        elif i == n_lig - 1 and j == n_col - 1:
            coordinates.append((i, j - 1))
            coordinates.append((i - 1, j))
        elif i == 0:
            coordinates.append((i, j + 1))
            coordinates.append((i, j - 1))
            coordinates.append((i + 1, j))
        elif j == 0:
            coordinates.append((i, j + 1))
            coordinates.append((i + 1, j))
            coordinates.append((i - 1, j))
        elif i == n_lig - 1:
            coordinates.append((i, j + 1))
            coordinates.append((i, j - 1))
            coordinates.append((i - 1, j))
        elif j == n_col - 1:
            coordinates.append((i, j - 1))
            coordinates.append((i + 1, j))
            coordinates.append((i - 1, j))
        else:
            coordinates.append((i, j + 1))
            coordinates.append((i, j - 1))
            coordinates.append((i + 1, j))
            coordinates.append((i - 1, j))

        return coordinates

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"


sol = Solution()
print(sol.exist(board,word))