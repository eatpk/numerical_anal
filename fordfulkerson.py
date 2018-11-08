#!/usr/bin/env python3
import networkx as nx

# no other imports allowed


def initialize_flow(graph):
    """Initialize a zero flow on a directed graph.

    Args:
        graph (networkx.DiGraph): Directed graph provided as a
        networkx.DiGraph object. Nodes are labeled from 0 to n-1, where n
        is the number of nodes in the graph. Each arc in the graph has an
        integer attribute "capacity", which represents the capacity of the
        arc. The capacity of arc (i,j) in graph is accessed with
         `graph[i][j]["capacity"]`.

    Returns:
        flow (dict): flow has a key (i,j) for every arc (i,j) in graph. Value
            flow[(i, j)] = 0 for all arcs.
    """
    flow={}
    for i in graph.edges:
        flow[i]=0
    return flow  # TODO: implement me


def initialize_residual_graph(graph):
    """Initialize residual graph for a directed graph.

    Initialize a residual grpah for the directed input graph. The residual
    graph assumes that the initial flow on each arc is zero. Input graph
    should not be changed.

    Args:
        graph (networkx.DiGraph): Directed graph provided as a
        networkx.DiGraph object. Nodes are labeled from 0 to n-1, where n
        is the number of nodes in the graph. Each arc in the graph has an
        integer attribute "capacity", which represents the capacity of the
        arc. The capacity of arc (i,j) in graph is accessed with
         `graph[i][j]["capacity"]`.

    Returns:
        residual_graph (networkx.DiGraph): Residual graph corresponding to the
            input graph with zero flow. The residual graph is defined on the
            same set of nodes and contains both the forward and reverse arcs
            for the arcs in the input graph. Forward arcs are initialized with
            residual capacity equal to the arc capacity. Reversed arcs are
            initialized with capacity 0 if the reverse arc is not present in
            the original graph. Nodes are labeled from 0 to n-1, where n is
            the number of nodes in the graph. Each arc in the graph has an
            integer attribute "residual", which represents the residual
            capacity along the arc. The residual capacity of arc (i,j) in
            residual_graph is accessed with `residual_graph[i][j]["residual"]`.
    """
    residual_graph= nx.DiGraph()
    
    residual_graph.add_nodes_from(graph)
    try:
        graph.edges
        for (i,j) in graph.edges:
            residual_graph.add_edge(i,j, residual=graph[i][j]["capacity"])
            try:
                residual_graph[j][i]["residual"]
            except:
                residual_graph.add_edge(j,i, residual=0)
    except:
        for i in graph.nodes:
            residual_graph.add_node(i)
        print(residual_graph)
    return residual_graph  # TODO: implement me



def update_residual_graph(resid_graph, path, value):
    """Update capacity of forward and backward arcs for augmenting path.

    Update residual graph in place. Residual capacity is decreased by value
    for arcs on the augmenting path. Residual capacity for arcs in reversed
    direction is increased by value.

    Args:
        resid_graph (nx.DiGraph): Residual graph to update. Graph is updated
            in place (without copying).
        path (list of tuples): List of arcs on augmenting path from s to t.
            Each arcs (i,j) is represented by tuple (i,j).
        value (int): Bottleneck flow on augmenting path.

    Returns:
        None
    """
    for (i,j) in path:
        resid_graph[i][j]["residual"]=resid_graph[i][j]["residual"]-value
        resid_graph[j][i]["residual"]=resid_graph[j][i]["residual"]+value
       
    return None  # TODO: implement me


def update_flow(flow, path, value):
    """Augment flow in original graph along augmenting path.

    Update flow for each arc on the augmenting path. If arc (i,j) is on the
    augmenting path, then we can either increase the flow along arc (i,j) or
    decrease the flow along arc (j,i) in the original graph (defined by the
    arcs in the dict flow). If (j,i) is in the original graph, then it first
    reduces the flow along (j,i) as much as possible. The remaining capacity
    is used to increase the flow along arc (i,j). This method ensures that the
    at least one of arcs (i,j) and (j,i) will have zero flow. It also ensures
    that the capacity for both arcs is always satisfied.

    Args:
        flow (dict): Dictionary with flow on the original graph. Keys are
            tuples (i,j) for every arc (i,j) in the original graph. Value is the flow on the arc. Flow is updated in place.
        path (list of tuples): List of arcs on the augmenting path.
        value (int): Bottleneck capacity of the augmenting path.

    Returns:
        None
    """
    
    for (i,j) in path:
        
        try:
            flow[(j, i)]
            
            if flow[(j,i)]>=0:
                a=flow[(j,i)]
                flow[(j,i)]=max(flow[(j,i)]-value,0)
                try:
                    flow[(i,j)]
                
                    if flow[(i,j)]>=0:        
                        flow[(i,j)]=flow[(i,j)]+max(value-a,0)
                except:
                    None
        
        except:
            flow[(i,j)]=flow[(i,j)]+value
            
    
    return None  # TODO: implement me


def breadth_first_search(graph, root):
    """Construct BFS tree on arcs with non-zero residual capacity from root.

    Applies BFS starting from root. Arcs with zero residual capacity are ignored.

    Args:
        graph (nx.DiGraph): Graph for which to construct BFS tree. Nodes must
            be indexed from 0 to n-1, where n is the number of nodes in the
            graph. Each arc must have an integer attribute "residual" for the
            residual capacity.
        root (int): Index of root node for the BFS tree.

    Returns:
        predecessors (list): List containing the parent of every node in the
            BFS tree. The parent for the source node and unreachable nodes is
            None.
    """
    visited = [False] * (len(graph))
    pred=[None]* (len(graph))

    queue = [] 

    queue.append(root) 
    visited[root] = True
  
    while queue: 
  
        s = queue.pop(0) 
        
        for i in graph.neighbors(s): 
            if visited[i] == False and graph[s][i]["residual"]>0: 
                queue.append(i) 
                visited[i] = True
                pred[i]=s
    return pred  # TODO: implement me


def find_augmenting_path(resid_graph, source, sink):
    """Find augmenting path with BFS.

    Finds a path from source to sink on the residual graph. The path is found
    with BFS.

    Args:
        resid_graph (nx.DiGraph): Residual graph. Arcs must have an integer attribute "residual" to denote the residual capacity of an arc.
        source (int): Index of source node.
        sink (int): Index of sink node.

    Returns:
        path (list of tuples): List of arcs on the augmenting path. Returns
            None if the sink is not reachable from the source.
        value (int): Bottleneck capacity of the augmenting path. It is defined
            as the minimum residual capacity of the arcs on the augmenting
            path. Returns None if the sink is unreachable from the source.
    """
    pred=breadth_first_search(resid_graph,source)
    index=sink
    path=[]
    value=float('inf')
    if pred[sink]!=None:
        while index!=source:
            a=pred[index]
            path.insert(0,(a,index))
            index=a
        for (i,j) in path:
            value=min(value,resid_graph[i][j]["residual"])
    else:
        return None, None
    
    return path, value  # TODO: implement me


def ford_fulkerson(graph, source, sink):
    """Finds the maximum flow from source to sink in a directed graph.

    Applies Ford-Fulkerson algorithm to find a maximum flow from source to
    sink in a directed graph. The flow on each arc must be non-negative and
    satisfy the capacity constraint.

    Args:
        graph (networkx.DiGraph): Directed graph provided as a
            networkx.DiGraph object. Nodes are labeled from 0 to n-1, where n
            is the number of nodes in the graph. Each arc in the graph has an
            integer attribute "capacity", which represents the capacity of the arc. The capacity of arc (i,j) in graph is
            accessed with `graph[i][j]["capacity"]`.
        source (int): Index of the source node. Must be an integer between 0
            and n-1.
        sink (int): Index of the sink node. Must be an integer between 0
            and n-1 and different from the index of the source node.

    Returns:
        A tuple of (value, flow).
        flow_value <int>: Value of the maximum flow.
        flow <dict>: Flow on each arc. The keys for the dictionary are arcs
            represented as tuples. The value <int> is the flow on the arc.

    Example:
        Graph with nodes [0, 1, 2] and the following set of arcs denoted as (u, v): capacity[u,v]
        {
            (0, 1): 1,
            (0, 2): 2,
            (1, 2): 3,
        },
        source = 0, source = 2

        >> value = 3
        >> flow = {
            (0, 1): 1,
            (0, 2): 2,
            (1, 2): 1,
    }
    """
    # initialize residual graph and flow
    residual_graph = initialize_residual_graph(graph)
    flow = initialize_flow(graph)
    flow_value = 0

    while True:
        path, path_value = find_augmenting_path(residual_graph, source, sink)
        if path_value is None:
            # stop. no path found. Optimal flow.
            break
        else:
            # update residual graph & flow.
            update_residual_graph(residual_graph, path, path_value)
            update_flow(flow, path, path_value)
            flow_value += path_value

    return (flow_value, flow)
