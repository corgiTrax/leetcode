class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    if j == 0 or grid[i][j-1] == 0: perimeter += 1 # west
                    if j == len(row) - 1 or grid[i][j+1] == 0: perimeter += 1 # east
                    if i == 0 or grid[i-1][j] == 0: perimeter += 1 # north
                    if i == len(grid) - 1 or grid[i+1][j] == 0: perimeter += 1 # south
        return perimeter

# a faster solution, only look at down and right neighbors
class Solution1(object):
    def islandPerimeter(self, grid):
        island = drneighbors = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 1:
                    island += 1
                    if i != len(grid) - 1 and grid[i+1][j] == 1: drneighbors += 1 # south
                    if j != len(row) - 1 and grid[i][j+1] == 1: drneighbors += 1 # east
        return island * 4 - drneighbors * 2

if __name__ == '__main__':
    sol = Solution1()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(sol.islandPerimeter(grid))
