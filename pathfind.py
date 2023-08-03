from typing import *


Node = TypeVar('Node')
Distance = int
Neighbours = List[Tuple[Node, Distance]]
NodeMap = Dict[Node, Neighbours]
Path = List[Node]
RequestedPath = Tuple[Node, Node]

new_map : NodeMap = {
    '1': [('3', 3), ('5', 2)], 
    '2': [('3', 5), ('4', 3)], 
    '3': [('1', 3), ('2', 5), ('4', 7)], 
    '4': [('2', 3), ('3', 7), ('6', 4), ('7', 4)], 
    '5': [('1', 2)],
    '6': [('4', 4), ('8', 10)],
    '7': [('4', 4)],
    '8': [('6', 10)]
}


class Path:

    def __init__(self, node_map: NodeMap) -> None:
        self.node_map = node_map
    
    def is_neighbour(self, selected_nodes: RequestedPath) -> bool:
        return selected_nodes[0] in [node for node, weight in self.node_map[selected_nodes[1]]]

    def get_neighbours(self, node: Node) -> List[Node]:
        return [n for n, weight in self.node_map[node]]

    def get_neighbour_weight(self, selected_nodes: RequestedPath) -> Distance:
        return [weight for node, weight in self.node_map[selected_nodes[0]] if node == selected_nodes[1]].pop()
    

    def get_all_paths(self, selected_nodes: RequestedPath, visited_neighbours: List[Node] = []) -> List[Path]:


        start, end = selected_nodes

        if self.is_neighbour(selected_nodes):
            return [[start, end]]
        
        start_neighbours = self.get_neighbours(start)


        paths = []
        for neighbour in start_neighbours:
            if neighbour in visited_neighbours:
                continue


            paths_from_neighbour = self.get_all_paths((neighbour, end), visited_neighbours + [start])
            
            for path in paths_from_neighbour:
                paths.append([start] + path)


        return paths


    def shortest_path(self, selected_nodes: RequestedPath) -> Path:


        start, end = selected_nodes
        all_paths = self.get_all_paths(selected_nodes)
        weights = []

        for path in all_paths:
            weight = 0

            for i, node in enumerate(path[:-1]):
                
                weight += self.get_neighbour_weight((node, path[i+1]))
            weights.append((path, weight))
        
        
        weights.sort(key = lambda x: x[1])
        return weights[0][0]



path = Path(new_map)
findPath = ('8', '5')

print(path.shortest_path(findPath))


