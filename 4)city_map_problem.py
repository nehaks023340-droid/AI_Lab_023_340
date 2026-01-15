from collections import deque

# City map represented as a graph
city_map = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

def bfs(start, goal):
    queue = deque([[start]])   # store paths
    visited = set()

    while queue:
        path = queue.popleft()
        city = path[-1]

        if city == goal:
            return path

        if city not in visited:
            visited.add(city)
            for neighbor in city_map[city]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# Run the search
start_city = 'A'
goal_city = 'G'

result = bfs(start_city, goal_city)
print("Path from", start_city, "to", goal_city, ":", result)
