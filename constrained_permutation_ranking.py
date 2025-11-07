"""
Members of the group: Zirui Fang, Hao Guo (alphabetical order)
assignment_1_Ex2.py: The code performs topological sort on a directed graph using DFS and calculates
                   the Trotter-Johnson rank of the resulting permutation. It reads restrictions pairs
                   to build the graph, checks for cycles, and outputs either a valid topological order
                   with its rank or indicates if the conditions are impossible to satisfy.
"""
# The function to give a list of element in topological sort
def topological_sort_dfs(n, G_l):
    """Perform topological sort using DFS and return the valid ordering if possible"""
    visited = [False] * (n + 1)  # To track visited nodes
    result = []  # This will store the topological sort
    in_stack = [False] * (n + 1)  # To track nodes in the current DFS stack (for cycle detection)

    def dfs(v):
        """Recursive DFS helper function"""
        in_stack[v] = True
        visited[v] = True
        for neighbor in G_l[v]:
            if not visited[neighbor]:
                if not dfs(neighbor):  # If a cycle is found
                    return False
            elif in_stack[neighbor]:  # Found a back edge (cycle)
                return False
        result.append(v)  # Add to result after finishing the node
        in_stack[v] = False
        return True

    # Perform DFS for every node
    for i in range(1, n + 1):
        if not visited[i]:
            if not dfs(i):
                return None  # Cycle detected, no valid ordering

    return result[::-1]  # Reverse the result to get the topological ordering

# We cite trotter_johnson_rank_recursive code from Permutation Generation, which is provided by professor Pablo Ezequiel TERLISKY on Moodle 
def trotter_johnson_rank_recursive(perm: list) -> int:
    """
    Calculates the rank of perm for numbers {1,..,len(perm)} for the Trotter-Johnson order recursively
    """
    rank = 0
    n = len(perm)
    if n > 1:
        k = 0
        while perm[k] != n:
            k += 1  # We find where n is in the permutation
        high_perm = []
        if k < n - 1:
            high_perm = perm[k + 1:]
        rec_perm = perm[:k] + high_perm  # The numbers at the right of n will be moved one place to the left
        rec_rank = trotter_johnson_rank_recursive(rec_perm)  # Recursively calculate the rank of the new permutation
        if rec_rank % 2:  # According to whether the recursive permutation was odd or even
            rank = n * rec_rank + k
        else:
            rank = n * rec_rank + (n - 1 - k)
    return rank

# Ask the user that they want to see the test examples from the assignment and ours, or they want to test their own cases
print("Enter True, if you want see the examples from the assignment and ours.")
print("Enter False, if you want to test your own cases.")
RUN_TEST = input() # input True -> "True"

# If RUN_TEST = True, then run the code of testing cases
if RUN_TEST == "True":
    # test_case_1 is the first example provided in the Exercise2
    test_case_1 = [10,8,(2,3),(4,5),(1,2),(1,4),(2,4),(7,8),(4,7),(3,6)]
    
    # test_case_2 is the second example provided in the Exercise2
    test_case_2 = [5,5,(1,2),(2,3),(5,3),(3,4),(4,1)]
     
    # test_case_3 is an example of permutations for numbers from 1 to 8 and has 6 restrictions and be possible to satisfy
    test_case_3 = [8,6,(1,2),(2,3),(4,5),(3,6),(5,7),(6,8)]
    
    # test_case_4 is an example of permutations for numbers from 1 to 8 and has 6 restrictions and be impossible to satisfy
    test_case_4 = [8,6,(1,2),(2,3),(3,4),(4,2),(4,5),(5,6)]
    
    # Prints out all the results of these 4 cases
    for case in [test_case_1,test_case_2,test_case_3, test_case_4]:
            n, m = case[0], case[1]
            # We cite adjacency list representation code from Graph Algorithms, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
            # Adjacency List Representation
            # Initialization
            G_l = []
            for i in range(n + 1):
                G_l.append([])
            # Adding all the restrictions
            for (a,b) in case[2:]:
                G_l[a].append(b)
            
            # Perform topological sort
            valid_ordering = topological_sort_dfs(n, G_l)
            
            print(f"\nThe number of vertices: {n}, The number of restrictions: {m}")
            print("The restrictions pairs are:",[(a,b) for (a,b) in case[2:]])
            
            if not valid_ordering:
                print("Result: Impossible to satisfy the conditions")
            else:
                rank = trotter_johnson_rank_recursive(valid_ordering)
                print("Topological Sort:", valid_ordering)
                print("Trotter-Johnson Rank:", rank)
       
# If RUN_TEST = False, then run the code of manual input
else:
    print("\nEnter graph data:")
    line = input()         # input 10 8 -> "10 8" 
    parts = line.split()   # "10 8".split() -> ["10", "8"]
    n = int(parts[0])      # n = int("10") = 10
    m = int(parts[1])      # m = int("8") = 8

    # We cite adjacency list representation code from Graph Algorithms, which is provided by professor Pablo Ezequiel TERLISKY on Moodle
    # Adjacency List Representation
    # Initialization
    G_l = []
    for i in range(n + 1):
        G_l.append([])

    # Adding all restrictions
    for i in range(m):
        perm_line = input()         # input 2 3 -> "2 3" 
        perm_parts = perm_line.split()   # "2 3".split() -> ["2", "3"]
        a = int(perm_parts[0])      # n = int("2") = 2
        b = int(perm_parts[1])      # m = int("3") = 3
        G_l[a].append(b)

    # Perform topological sort
    valid_ordering = topological_sort_dfs(n, G_l)

    if not valid_ordering:
        print("Impossible to satisfy the conditions")  # No valid permutation exists
    else:
        # Calculate the rank of the valid permutation
        rank = trotter_johnson_rank_recursive(valid_ordering)
        print("Topological Sort:", valid_ordering)
        print("Trotter-Johnson Rank:", rank)
