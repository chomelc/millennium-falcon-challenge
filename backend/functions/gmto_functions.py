import sys
import os
import math
import networkx as nx
from networkx.classes.function import path_weight
from db_functions import create_connection, select_all_routes
from empire import Empire
from millennium_falcon import MillenniumFalcon


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


def compute_odds(empire_file, millennium_falcon_file="millennium-falcon.json"):
    """Computes the odds of the Falcon's mission to succeed.
    @param `empire_file`: the `empire.json` file
    @param `millennium_falcon_file`: the `millennium-falcon.json` file, 
        if not provided, it uses the default one stored in `backend/` 
    @return the computed odds
    """
    mf = MillenniumFalcon(millennium_falcon_file)
    empire = Empire(empire_file)

    db = f"{os.environ.get('MFC_PATH')}/backend/{mf.get_routes_db()}"
    cnx = create_connection(db)
    cur = cnx.cursor()

    graph = create_graph(cur)
    cnx.close()

    all_paths_info = get_all_paths_info(
        graph, mf.get_departure(), mf.get_arrival())

    for path_info in all_paths_info:
        # for all simple paths
        fuel = autonomy = mf.get_autonomy()
        countdown = empire.get_countdown()
        bounty_hunters = empire.get_bounty_hunters()
        path = path_info["path"]
        current_day = 0
        met_bounty_hunters = 0

        for index in range(len(path) - 1):
            # for all routes
            distance = (graph[path[index]][path[index + 1]])["weight"]
            current_day += distance

            # if the Millennium Falcon waits on a planet,
            # refuel anyway
            if (path[index + 1] == f"{path[index]}Bis"):
                # refuel
                fuel = autonomy
            else:
                fuel -= distance

            # check if there is a bounty hunter on this neighbor
            # planet at the time of the Millennium Falcon's visit
            if (any((d['planet'] == path[index + 1] or d['planet'] == path[index + 1][:-3]) for d in bounty_hunters)
                    and any(d['day'] == current_day for d in bounty_hunters)):
                met_bounty_hunters += 1
                path_info["mission_success"] = float(mission_success(
                    met_bounty_hunters))

            # if the travel_time exceeds the countdown
            # or the Millennium Falcon did not refuel when needed,
            # the mission fails
            if path_info["total_travel_time"] > countdown or fuel < 0:
                path_info["mission_success"] = 0

    # print(max(all_paths_info, key=lambda x: x['mission_success']))
    return max(path["mission_success"] for path in all_paths_info)


def create_graph(cur):
    """Creates a weighted graph of the planets, with the planets being nodes 
    and the travel time between two planets being the weight of the edge 
    between the corresponding nodes
    @param `cur`: the `Connection`\'s cursor
    @param `indexes`: the dict containing the association of the planets with indexes
    @return the networkx `Graph`
    """
    G = nx.Graph()
    for row in select_all_routes(cur):
        G.add_edge(row[0], row[1], weight=row[2])
        # adding "bis" nodes to deal with the
        # fact of staying on a planet
        G.add_edge(row[0], f"{row[0]}Bis", weight=1)
        G.add_edge(f"{row[0]}Bis", row[1], weight=row[2])
    return G


def get_all_paths_info(graph, source, target):
    all_paths_info = []
    for path in nx.all_simple_paths(graph, source, target):
        all_paths_info.append(
            {"path": path, "total_travel_time": path_weight(graph, path, weight="weight"), "mission_success": 100})
    return all_paths_info


# defining a main to be used with the CLI
if __name__ == '__main__':
    print(compute_odds(sys.argv[2], sys.argv[1]))
