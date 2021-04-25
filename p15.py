from collections import deque

g = [[1, 4, 6],
    [2, 3, 4],
    [0],
    [2, 3, 5],
    [0, 1],
    [4],
    [3,4]]


def bfs(graph, root):
    queue, visited, trace = deque([root]), {root}, [root]

    while queue:
        node = queue.popleft()
        for children in graph[node]:
            if children not in visited:
                visited.add(children)
                queue.append(children)
                trace.append(children)
    return trace

def dfs(graph, root):
    stack, visited, trace = [root], set(), []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack += reversed(graph[node])
            trace.append(node)
    return trace