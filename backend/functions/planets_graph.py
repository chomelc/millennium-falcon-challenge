from queue import PriorityQueue


class Graph:
    """A class used to represent a graph.
    """

    def __init__(self, num_of_vertices):
        """Constructs the Graph object with the specified number of vertices.
        @param `num_of_vertices`: number of vertices
        """
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)]
                      for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        """Adds a weighed edge to the Graph object, between the `u` and the `v` nodes.
        @param `u`: the origin node
        @param `v`: the destination node
        @param `weight`: the weight of the edge
        """
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    """Returns the shortests paths between nodes of the graph with `start_vertex` 
    as the origin, using the Dijkstra algorithm.
    @param `graph`: the graph to evaluate
    @param `start_vertex`: the origin node from which the alogirhtm 
    calculates the shortest paths
    """
    D = {v: float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def navigate_graph(graph, start_vertex, autonomy, bounty_hunters, countdown):
    """Navigates the graph, determines the best path and returns 
    the computed odds of that path.
    @param `graph`: the graph to navigate into
    @param `start_vertex`: the origin node from which the alogirhtm 
    navigates the graph
    @param `autonomy`: the autonomy of the Millennium Falcon
    @param `bounty_hunters`: locations and days where Bounty Hunters have planned to 
    hunt the Millennium Falcon
    @param `countdown`: number of days before the Death Star annihilates Endor
    @return the computed odds of the best path 
    """
    total_travel_time = 0
    return 42
