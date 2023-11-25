def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {"Erik": {"Alex", "Minnie", "John"},
         "Alex": {"Fiola", "Erik"},
         "Fiola": {"Alex", "Nick"},
         "Nick": {"Fiola"},
         "John": {"Erik"},
         "Minnie": {"Erik"}}

print(dfs(graph, "Erik"))
