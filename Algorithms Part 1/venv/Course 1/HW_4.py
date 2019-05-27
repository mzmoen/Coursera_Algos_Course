import random
import copy
import csv


def read_file():
    with open("HW_4_TextFile.txt", "r") as f:
        return [[j for j in i.split('\t') if j != ''] for i in f.read().split('\n')]


def contraction(graph_input):
    length = len(graph_input)
    if length == 2:
        return len([x for x in graph_input[0] if x != graph_input[0][0]])
    else:
        vertex1_array = graph_input.pop(random.randrange(len(graph_input)))
        vertex1 = vertex1_array[0]
        vertex2 = random.choice([x for x in vertex1_array if x != vertex1])

        vertex2_array = next(vertex for vertex in graph_input if vertex[0] == vertex2 and vertex[0] != vertex1)
        graph_input.remove(vertex2_array)
        vertex2_adj_required = [x for x in vertex2_array if x != vertex2 and x != vertex1]
        vertex1_array.extend(vertex2_adj_required)
        graph_input.append(vertex1_array)

        for idx, vertex in enumerate (graph_input):
            if vertex2 in vertex:
                vertex[:] = [x if x != vertex2 else vertex1 for x in vertex]

        return contraction(graph_input)


graph = [[1, 2, 3, 4, 7], [2, 1, 3, 4], [3, 1, 2, 4], [4, 1, 2, 3, 5], [5, 4, 6, 7, 8], [6, 5, 7, 8],
        [7, 1, 5, 6, 8],
        [8, 5, 6, 7]]


def looping(graph_input):
    min_cut = []
    for _ in range(len(graph_input)*10):
        graph_use = copy.deepcopy(graph_input)
        min_cut.append(contraction(graph_use))
    print(min(min_cut))



looping(read_file())

# sort out returning and selecting min when looping through, and use read_file
# for _ in range(100):
#     graph = [[1, 2, 3, 4, 7], [2, 1, 3, 4], [3, 1, 2, 4], [4, 1, 2, 3, 5], [5, 4, 6, 7, 8], [6, 5, 7, 8],
#              [7, 1, 5, 6, 8],
#              [8, 5, 6, 7]]
#     print(contraction(graph))