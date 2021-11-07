directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

print(list(map(lambda x,y:x+y, directions[0], directions[1])))