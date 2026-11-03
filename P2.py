#T.C=O(n^2) S.C=O(n^2)
grid = [
['S', '.', 'X'],
['X', '.', '.'],
['.', '.', 'G']
]
# Start position
row = 0
col = 0
# Internal state (memory)
visited = []
while True:
    visited.append((row, col))
    print("Current Position:", (row, col))
    # Goal reached
    if grid[row][col] == 'G':
        print("Goal Reached!")
        print("total steps:",len(visited)-1)
        break
    # Move Right if possible
    if col < 2 and grid[row][col + 1] != 'X':
        col = col + 1
    # Otherwise Move Down
    elif row < 2 and grid[row + 1][col] != 'X':
        row = row + 1
    else:
        print("No Path Found!")
        break
print("Visited Cells:", visited)