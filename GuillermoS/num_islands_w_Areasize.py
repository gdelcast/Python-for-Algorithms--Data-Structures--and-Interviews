def  num_islands(grid):
    if not grid: return
    count = 0
    area = {}

    r = len(grid)
    c = len(grid[0])

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                count+=1
                area[count] = 0
                __visitIsland(grid, i, j, area, count)

    return [count, max(area.values())]  #return # of islands and area of largest island

def __visitIsland(grid, i, j, area, count):
    if grid[i][j] == '1':
        grid [i][j] = '0'
        area[count] += 1
        if i-1>=0:
            __visitIsland(grid, i-1, j, area, count)
        if j-1>=0:
            __visitIsland(grid, i, j-1, area, count)
        if i+1<len(grid):
            __visitIsland(grid, i+1, j, area, count)
        if j+1<len(grid[0]):
            __visitIsland(grid, i, j+1, area, count)


grid = []
grid.append(['1','1','1','1','0'])
grid.append(['1','1','0','1','0'])
grid.append(['0','0','1','0','0'])
grid.append(['0','0','0','1','1'])

# grid.append(['1','1','1','1','0'])
# grid.append(['1','1','1','1','0'])
# grid.append(['0','0','1','1','0'])
# grid.append(['0','0','0','1','1'])

#print(grid)
print(num_islands(grid))