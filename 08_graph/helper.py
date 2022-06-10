"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def create_graph(adj_list):
    """
    e.g.  adj_list = [[2,4],[1,3],[2,4],[1,3]]
    """
    visited = {}
    for i, adj in enumerate(adj_list):
        if not visited.get(i+1, None):
            node = Node(i+1)
            visited[i+1] = node
        else:
            node = visited[i+1]

        for val in adj:
            if visited.get(val, None):
                node.neighbors.append(visited[val])
            else:
                neighbor = Node(val)
                visited[val] = neighbor
                node.neighbors.append(neighbor)
    return visited[1]