def bfs(graph, start: str) -> list:
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

graph = {"Erik": ["Alex", "Minnie", "John"],
         "Alex": ["Fiola", "Erik"],
         "Fiola": ["Alex", "Nick"],
         "Nick": ["Fiola"],
         "John": ["Erik"],
         "Minnie": ["Erik"]}

print(bfs(graph, "Erik"))
