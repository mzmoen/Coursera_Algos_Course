edge_list = []

#####################
# Read input in
file = open("HW1_Part3_Data.txt", "r")
data = file.readlines()

for line in data:
    edge_list.append(list(map(int, line.strip('\n').split())))

# print(edge_list)

visited = [1]
shortest_edge_list = []

while edge_list[0][0] != len(visited):
    shortest_vertex = 0
    shortest_edge = 999999999999
    for x in edge_list[1:]:
        if ((x[0] in visited and not x[1] in visited) or (x[1] in visited and not x[0] in visited)) and x[2] < shortest_edge:
            if x[0] in visited:
                shortest_vertex = x[1]
            else:
                shortest_vertex = x[0]
            shortest_edge = x[2]
    # print(shortest_vertex, shortest_edge)
    visited.append(shortest_vertex)
    shortest_edge_list.append(shortest_edge)

# print(visited)
print(sum(shortest_edge_list))



