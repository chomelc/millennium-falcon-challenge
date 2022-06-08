import math
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


def capture_probability(met_bounty_hunters):
    """Computes the total probability of being captured based on the 
    number of bounty hunters met.
    @param `met_bounty_hunters`: the number of bounty hunters met
    @return the total probability of being captured
    """
    sum = 0
    for n in range(0, met_bounty_hunters):
        sum += (math.pow(9, (n))) / (math.pow(10, n + 1))
    return sum


def mission_success(met_bounty_hunters):
    """Computes the total probability of the mission's success based on the 
    number of bounty hunters met.
    @param `met_bounty_hunters`: the number of bounty hunters met
    @return the total probability of the mission's success
    """
    return "{0:.2f}".format((1 - capture_probability(met_bounty_hunters)) * 100)


def navigate_graph(graph, start_vertex, target_vertex, autonomy, bounty_hunters, countdown):
    """Navigates the graph, determines the best path and returns 
    a list of paths with their cost (in days) and the odds of the mission's success.
    Note: the best path is not the shortest but the one with the best odds, 
    which takes the countdown into consideration.
    @param `graph`: the graph to navigate into
    @param `start_vertex`: the origin node from which the algorithm 
    navigates the graph
    @param `target_vertex`: the target node of the graph
    @param `autonomy`: the autonomy of the Millennium Falcon
    @param `bounty_hunters`: locations and days where Bounty Hunters have planned to 
    hunt the Millennium Falcon
    @param `countdown`: number of days before the Death Star annihilates Endor
    @return a list of paths with their cost (in days) and the odds of the mission's success
    """

    # the Millennium Falcon cannot go from Tatooine to Endor in less than 7 days in any way
    # if (empire.get_countdown() < shortest_paths[mf.get_arrival()]):
    #     return 0

    # the Millennium Falcon cannot go from Tatooine to Endor in 7 days or less
    # if its autonomy is less than 7 days
    # if (empire.get_countdown() == shortest_paths[mf.get_arrival()] and mf.get_autonomy() < shortest_paths[mf.get_arrival()]):
    #     return 0

    # the Millennium Falcon cannot go anywhere if its autonomy is less
    # than the travel time to the closest planet
    # if (mf.get_autonomy() < min(shortest_paths.values())):
    #     return 0

    result = []
    total_travel_time = 0
    met_bounty_hunters = 0
    fuel = autonomy
    time_left = countdown

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    print("TODO")
                    # old_cost = D[neighbor]
                    # new_cost = D[current_vertex] + distance
                    # if new_cost < old_cost:
                    #     pq.put((new_cost, neighbor))
                    #     D[neighbor] = new_cost
    graph.visited = []
    return 42
