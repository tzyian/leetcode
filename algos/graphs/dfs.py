def dfs(graph):
    visited = set()
    result = []

    def dfs_helper(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            dfs_helper(neighbor)

    for vertex in graph:
        if vertex not in visited:
            dfs_helper(vertex)

    return result


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result
