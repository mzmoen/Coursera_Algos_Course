
# Copyright David Bai: Anyone can use this code without permission or referencing the original source
"""
W1 Kosaraju Algorithm
List Based Iterative Implementation to find sizes of strongly connected components
"""

########################################################
# Data Structures

# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
num_nodes = 875715

# Adjacency representations of the graph and reverse graph
gr = [[] for i in range(num_nodes)]
r_gr = [[] for i in range(num_nodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * num_nodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * num_nodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("HW_1_Data.txt", "r") # I named the input file W1_SCC_edges.txt, but you can name it whatever you wish
data = file.readlines()

for line in data:
    items = line.split()
    gr[int(items[0])] += [int(items[1])]
    r_gr[int(items[1])] += [int(items[0])]


########################################################
# DFS on reverse graph
global t
t = 0
for node in range(num_nodes-1, 0, -1):
    if not visited[node]:
        for x in r_gr[node]:
            if not visited[x]:
                stack.insert(0, x)
        visited[node] = True
        stack.append(node)
    while stack:
        stack_node = stack[0]
        visited[stack_node] = True
        for head in r_gr[stack_node]:
            if not visited[head]:
                stack.insert(r_gr[stack_node].index(head), head)
                visited[head] = True
        if stack_node == stack[0]:
            t += 1
            order.insert(0, stack.pop(0))


########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable

for node in order:
    global s
    s = None
    if not visited[node]:
        s = node
        for x in gr[node]:
            if not visited[x]:
                stack.insert(0, x)
                visited[x] = True
        if not visited[node]:
            stack.append(node)
            visited[node] = True
    while stack:
        stack_node = stack[0]
        visited[stack_node] = True
        for head in gr[stack_node]:
            if not visited[head]:
                stack.insert(0, head)
                visited[head] = True
        if stack_node == stack[0]:
            scc[s] += 1
            stack.pop(0)
            # break


########################################################
# Getting the five biggest sccs
scc.sort(reverse=True)
print(scc[:5])

# 1 2
# 2 3
# 2 4
# 2 5
# 3 6
# 4 5
# 4 7
# 5 2
# 5 6
# 5 7
# 6 3
# 6 8
# 7 8
# 7 10
# 8 7
# 9 7
# 10 9
# 10 11
# 11 12
# 12 10
# Answer: 6,3,2,1,0


# 1 2
# 2 3
# 3 1
# 3 4
# 5 4
# 6 4
# 8 6
# 6 7
# 7 8
# Answer: 3,3,1,1,0