# A* Search for 8 Puzzle
#T.C=O(branching factor^depth) S.C=O(b^d)
import heapq

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count

def get_moves(state):
    result = []
    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new_pos = zero + move

        if 0 <= new_pos < 9:
            if abs(zero // 3 - new_pos // 3) + \
               abs(zero % 3 - new_pos % 3) == 1:

                new_state = list(state)
                new_state[zero], new_state[new_pos] = \
                    new_state[new_pos], new_state[zero]

                result.append(tuple(new_state))

    return result

queue = [(heuristic(start), 0, start, [start])]
visited = set()

while queue:
    f, cost, state, path = heapq.heappop(queue)

    if state in visited:
        continue
    visited.add(state)

    if state == goal:
        print("Solution found!")
        print("Number of moves:", cost)

        for s in path:
            print(s[:3])
            print(s[3:6])
            print(s[6:])
            print()
        break

    for next_state in get_moves(state):
        if next_state not in visited:
            new_cost = cost + 1
            heapq.heappush(
                queue,
                (new_cost + heuristic(next_state),
                 new_cost, next_state, path + [next_state])
            )
else:
    print("No solution found.")