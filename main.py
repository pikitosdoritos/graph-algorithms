graph_a = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"], 
    "F": ["B", "E"],
}

def find_path(graph, finish, path, omit_list=[]):
    current = path[-1]
    connected_nodes = list(filter(lambda node: node not in omit_list, graph[current]))
    
    if finish in connected_nodes:
        path.append(finish)
        return path
    
    for node in connected_nodes:
        result = find_path(graph_a, finish, [*path, node], omit_list=[*omit_list, *connected_nodes])
        
        if result:
            return result
        
    return None
    
    
print(find_path(graph_a, "A", ["E"]))