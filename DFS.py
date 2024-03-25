def dfs(graph, start, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == target:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, target, visited, path)
            if new_path:
                return new_path

    return None


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
target_value = 'F'

result = dfs(graph, start_node, target_value)

if result:
    print(
        f"Found target value '{target_value}' using DFS. Path: {' -> '.join(result)}")
else:
    print(f"Target value '{target_value}' not found using DFS.")
