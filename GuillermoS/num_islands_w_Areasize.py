from collections import deque
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
                #__visitIsland(grid, i, j, area, count)
                __visitBFS(grid, i, j)

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

def __visitBFS(grid, i, j):        
        nr = len(grid)
        nc = len(grid[0])

        if grid[i][j]=='1':

            grid[i][j]=='0'
            neighbors = deque([])
            neighbors.append(i * nc + j)
            
            while neighbors:
                n = neighbors.popleft()
                ni = n//nc
                nj = n%nc
                
                if ni-1>=0 and grid[ni-1][nj] =='1':
                    grid[ni-1][nj] ='0'
                    neighbors.append((ni-1)*nc+nj)
                    
                if ni+1<nr and grid[ni+1][nj] =='1':
                    grid[ni+1][nj] ='0'
                    neighbors.append((ni+1)*nc+nj)
                    
                if nj-1>=0 and grid[ni][nj-1] =='1':
                    grid[ni][nj-1] ='0'
                    neighbors.append(ni*nc+(nj-1))
                    
                if nj+1<nc and grid[ni][nj+1] =='1':
                    grid[ni][nj+1] ='0'
                    neighbors.append(ni*nc+(nj+1))


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