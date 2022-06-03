import sys
import os
from db_functions import create_connection, select_all_routes, select_all_unique_planets
from planets_graph import Graph, dijkstra, navigate_graph
from empire import Empire
from millennium_falcon import MillenniumFalcon


def compute_odds(empire_file, millennium_falcon_file="millennium-falcon.json"):
    """Computes the odds of the Falcon's mission to succeed.
    @param `empire_file`: the path to the `empire.json` file
    @param `millennium_falcon_file`: the path to the `millennium-falcon.json` file, 
        if not provided, it uses the default one stored in `backend/` 
    @return the computed odds
    """
    mf = MillenniumFalcon(millennium_falcon_file)
    empire = Empire(empire_file)

    db = f"{os.environ.get('MFC_PATH')}/backend/{mf.get_routes_db()}"
    cnx = create_connection(db)
    cur = cnx.cursor()
    indexes = create_indexes(cur)

    graph = create_graph(cur, indexes)
    cnx.close()

    shortest_paths = format_dijkstra_result(dijkstra(graph=graph,
                                                     start_vertex=indexes[mf.get_departure()]), indexes)

    # the Millennium Falcon cannot go from Tatooine to Endor in less than 7 days in any way
    if (empire.get_countdown() < shortest_paths[mf.get_arrival()]):
        return 0

    # the Millennium Falcon cannot go from Tatooine to Endor in 7 days or less
    # if its autonomy is less than 7 days
    if (empire.get_countdown() == shortest_paths[mf.get_arrival()] and mf.get_autonomy() < shortest_paths[mf.get_arrival()]):
        return 0

    # the Millennium Falcon cannot go anywhere if its autonomy is less
    # than the travel time to the closest planet
    if (mf.get_autonomy() < min(shortest_paths.values())):
        return 0

    return navigate_graph(graph=graph,
                          start_vertex=indexes[mf.get_departure()],
                          autonomy=mf.get_autonomy(),
                          bounty_hunters=empire.get_bounty_hunters(),
                          countdown=empire.get_countdown())


def create_indexes(cur):
    """Creates a dictionnary containing the association of planet names with indexes
    @param `cur`: the `Connection`\'s cursor
    @return the dict containing the association of the planets with indexes
    """
    indexes = {}
    index = 0
    for planet in select_all_unique_planets(cur):
        indexes[planet[0]] = index
        index += 1
    return indexes


def create_graph(cur, indexes):
    """Creates a weighed graph of the planets, with the planets being nodes 
    and the travel time between two planets being the weight of the edge 
    between the corresponding nodes
    @param `cur`: the `Connection`\'s cursor
    @param `indexes`: the dict containing the association of the planets with indexes
    @return the `Graph`
    """
    g = Graph(len(indexes))
    for row in select_all_routes(cur):
        g.add_edge(indexes[row[0]], indexes[row[1]], row[2])
    return g


def format_dijkstra_result(D, indexes):
    """Format the output the the Dijkstra algorithm by 
    replacing the indexes with actual names of the planets.
    @param `D`: the result of the Dijkstra algorithm
    @param `indexes`: the dict containing the association of the planets with indexes
    @return the formatted output of the Dijkstra algorithm
    """
    result = {}
    for key in D:
        result[list(indexes.keys())[
            list(indexes.values()).index(key)]] = D[key]
    # removing the origin (travel time = 0) from the result
    result = {key: val for key, val in result.items() if val != 0}
    return result


# defining a main to be used with the CLI
if __name__ == '__main__':
    print(compute_odds(sys.argv[2], sys.argv[1]))
