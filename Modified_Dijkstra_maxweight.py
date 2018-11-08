#!/usr/bin/env python3
import networkx as nx  # No other imports allowed.


def find_min(labels, temporary):
    """Find index of temporary node with lowest label.

    Implement the naive version of `find_min`. Ties are broken by returning
    the first temporary node with the minimum label.

    Args:
        labels (list): Distance labels of all nodes in the graph.
        temporary (list): List of booleans to indicate whether a node is
            temporary. If temporary[i] == True, then node i is temporary.
            The lists labels and temporary have the same length.

    Returns:
        int: Index of the temporary node with the minimum label in the list
            labels.
    """
    return None  # TODO: Implement me!


def initialize_dijkstra(graph, source):
    """Initializes labels, predecessors, and temporary nodes.

    See description of the returned lists for the correct initialization.

    Args:
        graph (networkx.DiGraph): Directed graph provided as a
            networkx.DiGraph object. Nodes are labeled from 0 to n-1, where n
            is the number of nodes in the graph. Each arc in the graph has an
            integer attribute "weight". The weight of arc (i,j) in graph is
            accessed with `graph[i][j]["weight"]`.
        source (int): Index of the source node. Must be an integer between 0
            and n-1.

    Returns:
        labels (list): Labels is a list with the distance labels of the nodes.
            It is initialized to zero for the source, w_{sj} for the
            outneighbors of source, and infinity - use float("inf") -
            otherwise.
        predecessors (list): List of predecessors on the minimum maximum
            weight paths. It is initialized to `source` for the out-neighbors
            of source and to `None` otherwise.
        temporary (list): The list marks whether a node is temporary. If the
            temporary[i] is True, then node i is temporary. It is intialized
            to a list of True booleans, except for the source index. The
            source node is marked as False.
    """
    return None, None, None  # TODO: Implement me!


def max_weight_dijkstra(graph, source):
    """Find minimum maximum weight paths from source to all nodes.

    Modified Dijkstra algorithm to find the minimum maximum weight path from a
    source node to all nodes in a directed graph. The algorithm returns both
    the minimum maximum weight along the path and the predecessor on the path
    for each node. The paths can be reconstructed from the list of
    predecessors. The minimum maximum weight from the source node to itself is
    assumed to be 0.

    Args:
        graph (networkx.DiGraph): Directed graph provided as a
            networkx.DiGraph object. Nodes are labeled from 0 to n-1, where n
            is the number of nodes in the graph. Each arc in the graph has an
            integer attribute "weight". The weight of arc (i,j) in graph is
            accessed with `graph[i][j]["weight"]`.
        source (int): Index of the source node. Must be an integer between 0
            and n-1.

    Returns:
        labels: List of maximum weights on the minimum max weight path from
            the source to all nodes. The maximum weight is `float('inf')` if
            the node is unreachable.

            Example:
            [ 0.0, 0.5, 1.0]
        predecessors: List of predecessors on the minimum max weight path from
            the source to all nodes. Returns None for the source or when a node
            is unreachable.

            Example:
            [ None, 0, 1]
    """
    # initialize dijkstra
    labels, predecessors, temporary = initialize_dijkstra(graph, source)
    # compute number of temporary nodes
    num_temp_nodes = len(graph.nodes) - 1

    # Process nodes until there are no more temporary nodes.
    while num_temp_nodes:
        # TODO: Implement me!
        num_temp_nodes = 0  # TODO: Delete this line (prevents an inf loop)

    return labels, predecessors
