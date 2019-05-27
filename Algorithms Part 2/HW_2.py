########################################################
# initializiation of vertex universe
vertices = [None] * 1

########################################################
# Importing the graphs
file = open("HW_2_Data.txt", "r")
data = file.readlines()

for line in data:
    items = line.strip('\n').split()
    vertices.insert(int(items[0]), [])
    for x in range(1, len(items), 1):
        vertices[int(items[0])].append(items[x].split(','))

########################################################

shortest_paths = [None] * (len(vertices))
processed_vertices = [False] * (len(vertices))

processed_vertices[0] = True
processed_vertices[1] = True
shortest_paths[1] = 0

while not all(processed_vertices):
    greedy_number = 9999999999999999999999999999
    greedy_next_vertex = 0
    end_flag = False
    for x in range(1, len(processed_vertices), 1):
        if processed_vertices[x]:
            for y in vertices[x]:
                if not processed_vertices[int(y[0])] and (int(shortest_paths[x]) + int(y[1])) < greedy_number:
                    greedy_number = int(shortest_paths[x]) + int(y[1])
                    greedy_next_vertex = int(y[0])
                    end_flag = True;
    shortest_paths[greedy_next_vertex] = greedy_number
    processed_vertices[greedy_next_vertex] = True
    if not end_flag:
        for x in range(1, len(processed_vertices), 1):
            if not processed_vertices[x]:
                shortest_paths[x] = 1000000
                processed_vertices[x] = True

for x in range(1, len(processed_vertices), 1):
    print(x, shortest_paths[x])

# 1	2,1	8,2
# 2	1,1	3,1
# 3	2,1	4,1
# 4	3,1	5,1
# 5	4,1	6,1
# 6	5,1	7,1
# 7	6,1	8,1
# 8	7,1	1,2
#
# output:
#
# 1 0 []
# 2 1 [2]
# 3 2 [2, 3]
# 4 3 [2, 3, 4]
# 5 4 [2, 3, 4, 5]
# 6 4 [8, 7, 6]
# 7 3 [8, 7]
# 8 2 [8]