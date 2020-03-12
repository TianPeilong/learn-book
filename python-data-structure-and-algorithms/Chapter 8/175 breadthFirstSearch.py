graph = {}
graph['A'] = ['B', 'G', 'D']
graph['B'] = ['A', 'F', 'E']
graph['C'] = ['F', 'H']
graph['D'] = ['F', 'A']
graph['E'] = ['B', 'G']
graph['F'] = ['B', 'D', 'C']
graph['G'] = ['A', 'E']
graph['H'] = ['C']

from collections import deque

def breadth_first_search(graph, root):
    visited_vertices = []
    graph_queue = deque([root])
    visited_vertices.append(root)
    while graph_queue:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remain_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remain_elements) > 0:
            for elem in sorted(remain_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)
    return visited_vertices

print(breadth_first_search(graph, 'A'))
