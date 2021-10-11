
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


        visited = self.getVisitedArray(grid)

        m = len(grid)
        n = len(grid[0])
        nb_of_islands = 0

        to_be_visited = []

        to_be_visited.append((0,0,False))

        while len(to_be_visited) > 0:
            current = to_be_visited.pop()
            i,j = current[0],current[1]
            if visited[(i,j)]:
                continue
            fromLand = current[2]
            value = grid[i][j]

            if not fromLand and value == "1":
                nb_of_islands += 1

            adj_coordinates = self.getAdjCoordinates(m, n, i, j,value)

            for coordinate in adj_coordinates:
                if not visited[(coordinate[0],coordinate[1])]:
                    if value == "1":
                        to_be_visited.append(coordinate)
                    else:
                        to_be_visited = [coordinate] + to_be_visited


            visited[(i,j)] = True

        return nb_of_islands


    def getAdjCoordinates(self,n_lig,n_col,i,j,value):
        coordinates = []
        if n_col == 1 and n_lig == 1:
            return coordinates
        elif n_lig == 1:
            if j == 0:
                coordinates.append((i, j + 1, value == "1"))
            elif j == n_col - 1:
                coordinates.append((i, j - 1, value == "1"))

            else:
                coordinates.append((i, j + 1, value == "1"))
                coordinates.append((i, j - 1, value == "1"))

        elif n_col == 1:
            if i == 0:
                coordinates.append((i + 1, j, value == "1"))
            elif i == n_lig - 1:
                coordinates.append((i - 1, j, value == "1"))
            else:
                coordinates.append((i + 1, j, value == "1"))
                coordinates.append((i - 1, j, value == "1"))


        elif i == 0 and j == 0:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
        elif i == 0 and j == n_col - 1:
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
        elif i == n_lig - 1 and j == 0:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i - 1, j, value == "1"))
        elif i == n_lig - 1 and j == n_col - 1:
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i - 1, j, value == "1"))
        elif i == 0:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
        elif j == 0:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
            coordinates.append((i - 1, j, value == "1"))
        elif i == n_lig - 1:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i - 1, j, value == "1"))
        elif j == n_col - 1:
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
            coordinates.append((i - 1, j, value == "1"))
        else:
            coordinates.append((i, j + 1, value == "1"))
            coordinates.append((i, j - 1, value == "1"))
            coordinates.append((i + 1, j, value == "1"))
            coordinates.append((i - 1, j, value == "1"))

        return coordinates


    def getVisitedArray(self,grid):
        visited = dict()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                visited[(i,j)] = False
        return visited




sol = Solution()

print(sol.numIslands([["1","0"]]))