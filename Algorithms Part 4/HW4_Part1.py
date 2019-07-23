def calc_2sat(file_name):

    # Read input in
    file = open(f"{file_name}", "r")
    data = file.readlines()

    num_nodes = 0

    for line in data[:1]:
        num_nodes = int(line.strip('\n'))

    gr = [[] for i in range(num_nodes * 2 + 1)]
    r_gr = [[] for i in range(num_nodes * 2 + 1)]

    # The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
    visited = [False] * (num_nodes * 2 + 1)

    # The list below holds info about sccs. The index is the node and the value is the scc leader.
    scc = [0] * (num_nodes * 2 + 1)

    graph_edges = []
    stack = []  # Stack for DFS
    order = []  # The finishing orders after the first pass

    for line in data[1:]:
        items = list(map(int, line.strip('\n').split()))
        if items[0] > 0:
            if items[1] > 0:
                graph_edges.append([items[0] + num_nodes, items[1]])
                graph_edges.append([items[1] + num_nodes, items[0]])
            if items[1] < 0:
                graph_edges.append([items[0] + num_nodes, abs(items[1]) + num_nodes])
                graph_edges.append([abs(items[1]), items[0]])
        elif items[1] > 0:
            graph_edges.append([abs(items[0]), items[1]])
            graph_edges.append([items[1] + num_nodes, abs(items[0]) + num_nodes])
        else:  # both negative
            graph_edges.append([abs(items[0]), abs(items[1]) + num_nodes])
            graph_edges.append([abs(items[1]), abs(items[0]) + num_nodes])

    # b = set(map(tuple, graph_edges))
    # graph_edges = list(map(list, b))

    for x in graph_edges:
        gr[int(x[0])] += [int(x[1])]
        r_gr[int(x[1])] += [int(x[0])]

    ########################################################
    # DFS on reverse graph
    for node in range(num_nodes * 2, 0, -1):
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
                order.insert(0, stack.pop(0))

    ########################################################
    # DFS on original graph
    print(order)
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
                if len(gr[node]) != 0:
                    stack.append(node)
                visited[node] = True
        while stack:
            stack_node = stack[0]
            visited[stack_node] = True
            for head in gr[stack_node]:
                if not visited[head]:
                    stack.insert(0, head)
                    visited[head] = True
            # if stack_node == stack[0] and len(gr[stack_node]) != 0:
            scc[stack_node] = s
            stack.pop(0)

    ########################################################
    for idx, x in enumerate(scc[:num_nodes + 1]):
        if x == scc[idx + num_nodes] and x != 0:
            print(file_name + ": Not going to work")
            break
    print(file_name + ": file processed")


# file_names = ["HW4_Data3.txt", "HW4_Data4.txt", "HW4_Data5.txt", "HW4_Data6.txt"]
#
# for x in file_names:
#     calc_2sat(x)

calc_2sat("HW4_Test.txt")

