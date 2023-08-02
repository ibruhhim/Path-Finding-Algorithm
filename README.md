# Path-Finding-Algorithm

This Path Finding Algorithm, helps users to determine the shortest paths from point A -> B on large scale node-maps, it can be used for various purposes including maze-running and GPS path finding.
<br>

## Algorithm

The path-finding algorithm utilizes a map represented as a dictionary, where each node is associated with its neighbors and the corresponding weights. The algorithm aims to determine the shortest paths between nodes in this map.

To use the algorithm, input data for any map in the form of a dictionary {Node: (Neighbour, Weight)}. This data represents the connections between nodes and the distance (weight) of each connection.

The algorithm employs recursion to navigate through neighboring nodes until it reaches the final destination. It continuously explores different paths from the starting node until it finds a direct path to the destination.

Upon reaching the destination, the algorithm gathers all the paths leading to it and returns them as a list of paths.

The path with the least weight is finally returned, in the form of a ordered list.

![newnodemap](https://github.com/IbrahimEllahi/Path-Finding-Algorithm/assets/85767913/cd1d2193-6f58-43e4-a941-0238a4d89307)
