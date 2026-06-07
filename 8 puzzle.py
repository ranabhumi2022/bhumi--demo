from collections import deque 


# ---------------- GOAL STATE ----------------//This is the final desired arrangement of the puzzle.


GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Possible movements of the blank tile  //Defines how the blank tile can move: Up/Down/LefT/Right
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# ---------------- FIND BLANK TILE ----------------//Finds the row and column position of the blank tile (0). Needed to know where moves are possible.

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# ---------------- GENERATE NEXT STATES ----------------// Creates all possible next puzzle states.

def generate_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


# ---------------- BFS ALGORITHM ----------------// This is the Breadth First Search algorithm.

def bfs(start_state):
    queue = deque([start_state])
    visited = {start_state}
    parent = {start_state: None}

    while queue:
        current = queue.popleft()  
        if current == GOAL_STATE:
            return reconstruct_path(parent, current)

        for neighbor in generate_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None


# ---------------- RECONSTRUCT PATH ----------------// Builds the solution path from goal to start using parent links.
def reconstruct_path(parent, state):
    path = []
    while state is not None:
        path.append(state)
        state = parent[state]
    path.reverse()
    return path


# ---------------- PRINT SOLUTION ----------------//Prints each puzzle configuration step-by-step.
def print_solution(path):
    for step in path:
        for row in step:
            print(row)
        print()


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    start_state = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    solution = bfs(start_state)

    if solution:
        print("Solution found in", len(solution) - 1, "moves:\n")
        print_solution(solution)
    else:
        print("No solution exists.")