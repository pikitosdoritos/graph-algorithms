graph_a = {
    "nodes": ["A", "B", "C", "D", "E", "F"],
    "edges": [
        ["A", "B"],
        ["A", "C"],
        ["B", "D"], 
        ["C", "D"], 
        ["C", "E"],
        ["E", "F"]        
    ]
}

def find_path(graph, trace, destination, omit_list=[]):
    if omit_list == []:
        omit_list.append(trace[0])
        
    location = trace[-1]
    node_connections = []
    
    for edge in graph["edges"]:
        if location in edge:
            node_connections.extend(filter(lambda node: node != location and node not in omit_list, edge))
            
    if destination in node_connections:
        return [*trace, destination]
    
    for node in node_connections:
        result = find_path(graph, [*trace, node], destination, [*omit_list, *node_connections])
        
        if result:
            return result
        
    return None

print(find_path(graph_a, ["A"], "E"))