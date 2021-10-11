
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


        visited,coming_from_land = self.getComingFromLandArrayAndVisitedArray(grid)
        m = len(grid)
        n = len(grid[0])
        nb_of_islands = 0

        to_be_visited = []

        to_be_visited.append((0,0))

        while len(to_be_visited) > 0:
            current = to_be_visited.pop(0)
            i,j = current[0],current[1]
            if visited[current]:
                continue
            value = grid[i][j]

            is_coming_from_land = coming_from_land[current]

            if not is_coming_from_land and value == "1":
                if self.isLandFromOtherSideAndNotVisited(i,j,grid,visited):
                    #to_be_visited = to_be_visited + [current]
                    visited[current] = True
                    continue
                nb_of_islands += 1

            adj_coordinates = self.getAdjCoordinates(m,n,i,j)

            for coordinate in adj_coordinates:
                if not visited[coordinate]:
                    to_be_visited.append(coordinate)

            visited[current] = True
        return nb_of_islands


    def getAdjCoordinates(self,n_lig,n_col,i,j):
        coordinates = []
        if i == n_lig - 1 and j == n_col - 1:
            return coordinates
        elif i == n_lig - 1:
            coordinates.append((i,j+1))
        elif j == n_col - 1:
            coordinates.append((i+1,j))
        else:
            coordinates.append((i, j + 1))
            coordinates.append((i + 1, j))
        return coordinates


    def getComingFromLandArrayAndVisitedArray(self,grid):
        visited = dict()
        coming_from_is_land = dict()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                visited[(i,j)] = False
                if i == 0 and j == 0:
                    coming_from_is_land[(i,j)] = False
                elif i == 0:
                    coming_from_is_land[(i,j)] = grid[i][j-1] == "1"
                elif j == 0:
                    coming_from_is_land[(i, j)] = grid[i-1][j] == "1"
                else:
                    coming_from_is_land[(i,j)] = grid[i-1][j] == "1" or grid[i][j-1] == "1"
        return visited,coming_from_is_land


        return visited,coming_from_is_land

    def isLandFromOtherSideAndNotVisited(self,i,j,grid,visited):
        n = len(grid)
        m = len(grid[0])

        if i == n - 1 and j == m - 1:
            return False
        elif i == n - 1:
            return grid[i][j+1] == "1" and not visited[(i,j+1)]
        elif j == m - 1:
            return grid[i+1][j] == "1" and not visited[(i+1,j)]
        else:
            return (grid[i + 1][j] == "1" and not visited[(i+1,j)]) or (grid[i][j + 1] == "1" and not visited[(i,j+1)])


sol = Solution()

print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))