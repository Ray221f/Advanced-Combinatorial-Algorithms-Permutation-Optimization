'''
Members of the group: Hao Guo, Zirui Fang
'''
import heapq
import math
# We cite dijkstra_queue(graph, s) code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def dijkstra_queue(graph, s):
    n = len(graph)
    distance = [float('inf')]*n
    parent = [-1]*n
    distance[s]=0
    parent[s]=s
    s_set = set()
    process_queue = []
    heapq.heappush(process_queue, (0,s))
    while process_queue:
        v = heapq.heappop(process_queue)[1]
        if not v in s_set:
            s_set.add(v)
            for (u,w,_) in graph[v]:
                if distance[v]+w < distance[u]:
                    distance[u] = distance[v]+w
                    parent[u] = v
                    heapq.heappush(process_queue,(distance[u],u))
    return (distance, parent)

# We cite dijkstra_vector(graph, s) code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def dijkstra_vector(graph, s):
    n = len(graph)
    distance = [float('inf')]*n
    parent = [-1]*n
    distance[s]=0
    parent[s]=s
    s_set = set()
    reachable_remaining = True
    while len(s_set)<n and reachable_remaining:
        min_dist = float('inf')
        v = None
        for i in range(n):
            if distance[i]<min_dist and (i not in s_set):
                min_dist = distance[i]
                v = i
        if min_dist == float('inf'):
            reachable_remaining = False
        else:
            s_set.add(v)
            for (u,w,_) in graph[v]:
                if distance[v]+w < distance[u]:
                    distance[u] = distance[v]+w
                    parent[u] = v
    return (distance, parent)

# Decide dense or sparse
def select_dijkstra_algorithm(n, m):
    V_squared = n * n
    if n > 1:
        E_log_V = m * math.log2(n) 
    else:
        E_log_V = 0
    if V_squared <= E_log_V:
        return dijkstra_vector
    else:
        return dijkstra_queue
    
# Build the shortest path from s to t
def build_path_s_to_t(parent, t, best_layer, n):
    target_node = t + best_layer * n
    path = []
    cur = target_node
    while parent[cur] != cur:
        path.append(cur % n)
        cur = parent[cur]
    path.append(cur % n)
    path.reverse()
    return path

# Construct layered graph
def build_layered_graph(E, n):
    new_n = 3 * n
    graph = [[] for _ in range(new_n)]
    
    # Add normal edges (within same layer)
    for u, v, w, p in E:
        if p == 0:  # Normal edge
            for layer in range(3):  # Add to all layers
                u_layer = u + layer * n
                v_layer = v + layer * n
                graph[u_layer].append((v_layer, w, 0))
    
    # Add special edges (across layers)
    for u, v, w, p in E:
        if p == 1:  # Special edge
            for layer in range(2):  # Connect layer i -> i+1
                u_layer = u + layer * n
                v_layer = v + (layer + 1) * n
                graph[u_layer].append((v_layer, w, 1))                
    return graph
    
# Standard input of graph
def read_graph_from_input():
    # The first line with n, m, s, t
    first_line = input().strip()
    n, m, s, t = map(int, first_line.split())

    # The following m lines with u, v, w, p
    E = []
    for _ in range(m):
        edge_line = input().strip()
        u, v, w, p = map(int, edge_line.split())
        E.append((u, v, w, p))

    return E, s, t, n

def main():
    E, s, t, n = read_graph_from_input()
    if n == 0:
        print("infeasible")
        return

    layered_graph = build_layered_graph(E, n)    
    new_n = 3 * n
    new_m = sum(len(adj) for adj in layered_graph)
    
    dijkstra = select_dijkstra_algorithm(new_n, new_m)
    distance, parent = dijkstra(layered_graph, s)
    
    targets = [t, t + n, t + 2 * n]
    min_dist = float('inf')
    best_layer = -1
    
    # Check three target destinations
    for layer, target in enumerate(targets):
        if distance[target] < min_dist:
            min_dist = distance[target] # Update min_dist
            best_layer = layer # Update best_layer
        # If two paths with different amount of special edges have the same length,
        # return the path with less special edges(smaller layer).
        elif distance[target] == min_dist and layer < best_layer:
            best_layer = layer
    
    if min_dist == float('inf'):
        print("infeasible")
        return
    
    path = build_path_s_to_t(parent, t, best_layer, n)
    
    print(f"({min_dist},{path})")

# Run the program
main()
