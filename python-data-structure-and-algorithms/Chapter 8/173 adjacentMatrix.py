graph = {}
graph['A'] = ['B', 'C']
graph['B'] = ['E','A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']

matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []

for key in matrix_elements:
    for neighbor in graph(key):
        edges_list.append((key, neighbor))

for edge in edges_list:
    col = matrix_elements.index(edge[0])
    row = matrix_elements.index(edge[1])
    adjacency_matrix[col][row] = 1