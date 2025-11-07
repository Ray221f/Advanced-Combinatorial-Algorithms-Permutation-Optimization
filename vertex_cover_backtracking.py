'''
Members of the group: Hao Guo, Zirui Fang (in arbitrary order)
Assignment_2_Ex3
'''
# We cite generate_adj_list_from_edge_list code from Shortest Path Algorithms.py, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
def generate_adj_list_from_edge_list(n, E, is_digraph=False):
    #Initialization
    G_l = []
    for _ in range(n):
        G_l.append([])
    #Adding all the edges
    for (u,v) in E:
        G_l[u].append(v)
        if not is_digraph:
            G_l[v].append(u)
    return G_l

# Standard input of graph
def read_graph_from_input():
    # The first line with n, m
    first_line = input().strip()
    n, m = map(int, first_line.split())

    # The following m lines with u, v
    E = []
    for _ in range(m):
        edge_line = input().strip()
        u, v = map(int, edge_line.split())
        E.append((u, v))

    return E, n

# Check if current x covers all edges
def is_valid_cover(x, E):
    for u, v in E:
        if x[u] == 0 and x[v] == 0:
            return False
    return True

# Solve vertex cover problem using backtracking with pruning
def vertex_cover_backtracking(E, n):
    G_l = generate_adj_list_from_edge_list(n, E, is_digraph=False) 
    x_opt = [1]*n     # Initialize optimal solution
    x_opt_size = n    # size of the optimal solution
    x_cur = [0]*n     # Initialize the current solution being explored
    
    # Check if we can skip selecting vertex i without leaving any edge uncovered.
    # Only checks edges with j < i (already processed vertices).        
    def can_skip_vertex(i):
        for j in G_l[i]:
            if j < i and x_cur[j] == 0:
                return False
        return True
    
    def backtrack(i, count):
        nonlocal x_opt, x_opt_size
        # Pruning by optimality, if current solution is already worse than optimal solution
        if count >= x_opt_size:
            return
        
        # Base case: all vertices processed
        if i == n:
            if is_valid_cover(x_cur, E): # Check if solution is valid
                x_opt_size = count        
                x_opt = x_cur.copy()
            return
        
        # Don't select current vertex (if feasible)
        if can_skip_vertex(i):
            # Option1: Don't select current vertex
            x_cur[i] = 0 # Update state
            backtrack(i+1,count)
            x_cur[i] = 0 # Restore state
            
            # Option2: select current vertex
            x_cur[i] = 1 # Update state
            backtrack(i+1, count + 1)
            x_cur[i] = 0 # Restore state
        
        # we must select current vertex (Pruning by feasibility)    
        if not can_skip_vertex(i):
            x_cur[i] = 1 # Update state
            backtrack(i + 1, count + 1)
            x_cur[i] = 0 # Restore state
    
    # Start backtracking from vertex 0 with 0 selected vertices
    backtrack(0,0)
    return x_opt_size, x_opt

def main():
    E, n = read_graph_from_input()
    x_opt_size, x_opt = vertex_cover_backtracking(E, n)
    print(f"({x_opt_size},{x_opt})")

# Run the program
main()
