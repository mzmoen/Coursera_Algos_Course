import sys

sys.setrecursionlimit(20000)

num_vertices = 0
num_edges = 0

edge_list = []

# Read input in
file = open("HW1_Part1_Data3.txt", "r")
data = file.readlines()

for line in data[:1]:
    num_vertices, num_edges = map(int, line.strip('\n').split())

value_store = {x: {y: 99999999999 for y in range(1, num_vertices + 1, 1)} for x in range(1, num_vertices + 1, 1)}

for line in data[1:]:
    edge_list.append(list(map(int, line.strip('\n').split())))

min_counter = 99999999

for x in edge_list:
    value_store[x[0]][x[1]] = x[2]
    min_counter = min(min_counter, x[2])

for x in range(1, num_vertices + 1, 1):
    value_store[x][x] = 0

counter_i = 1
counter_j = 1
counter_k = 1

while counter_k in range(num_vertices + 1):
    while counter_i in range(num_vertices + 1):
        while counter_j in range(num_vertices + 1):
            if value_store[counter_i][counter_k] + value_store[counter_k][counter_j] < value_store[counter_i][counter_j]:
                value_store[counter_i][counter_j] = value_store[counter_i][counter_k] + value_store[counter_k][counter_j]
                min_counter = min(min_counter, value_store[counter_i][counter_j])
                print(counter_k, counter_i, counter_j)
            counter_j += 1
        counter_j = 1
        counter_i += 1
    counter_j = 1
    counter_i = 1
    counter_k += 1

print(min_counter)

for x in range(1, num_vertices + 1, 1):
    if value_store[x][x] < 0:
        print("Negative cycle")


# def value_compare(i, j, k):
#     global min_counter
#     print(i, j, k)
#     if i not in value_store:
#         value_store[i] = {}
#     if j not in value_store[i]:
#         value_store[i][j] = {}
#     if i in value_store and j in value_store[i] and k in value_store[i][j]:
#         return value_store[i][j][k]
#     elif k == 0:
#         if i == j:
#             value_store[i][j][k] = 0
#             # return 0
#         elif [i, j] in [[x[0], x[1]] for x in edge_list]:
#             value_store[i][j][k] = [x[2] for x in edge_list if [x[0], x[1]] == [i, j]][0]
#             # return [x[2] for x in edge_list if [x[0], x[1]] == [i, j]][0]
#         else:
#             value_store[i][j][k] = 9999999999999999
#             # return 9999999999999999
#     # else:
#     #     return min(value_compare(i, j, k - 1), value_compare(k, j, k - 1) + value_compare(i, k, k - 1))
#     else:
#         value_store[i][j][k] = min(value_compare(i, j, k - 1), value_compare(k, j, k - 1) + value_compare(i, k, k - 1))
#     # if value_store[i][j][k] != 0 and value_store[i][j][k] < min_counter:
#     #     min_counter = value_store[i][j][k]
#     return value_store[i][j][k]
#
#
# def value_compare(i, j, k):
#     global min_counter
#     print(i, j, k)
#     if i not in value_store:
#         value_store[i] = {}
#     if i in value_store and j in value_store[i]:
#         return value_store[i][j]
#     elif k == 0:
#         if i == j:
#             value_store[i][j] = 0
#             # return 0
#         elif [i, j] in [[x[0], x[1]] for x in edge_list]:
#             value_store[i][j] = [x[2] for x in edge_list if [x[0], x[1]] == [i, j]][0]
#             # return [x[2] for x in edge_list if [x[0], x[1]] == [i, j]][0]
#         else:
#             value_store[i][j] = 9999999999999999
#             # return 9999999999999999
#     # else:
#     #     return min(value_compare(i, j, k - 1), value_compare(k, j, k - 1) + value_compare(i, k, k - 1))
#     else:
#         value_store[i][j][k] = min(value_compare(i, j, 0), value_compare(k, j, k - 1) + value_compare(i, k, k - 1))
#     # if value_store[i][j][k] != 0 and value_store[i][j][k] < min_counter:
#     #     min_counter = value_store[i][j][k]
#     return value_store[i][j][k]


# counter_i = 1
# counter_j = 1
# counter_k = 1
#
# while counter_i in range(num_vertices + 1):
#     while counter_j in range(num_vertices + 1):
#         while counter_k in range(num_vertices + 1):
#             min_counter = min(min_counter, value_compare(counter_i, counter_j, num_vertices))
#             counter_k += 1
#         counter_k = 1
#         counter_j += 1
#         print(counter_i, counter_j)
#     counter_k = 1
#     counter_j = 1
#     counter_i += 1

# while counter_i in range(num_vertices + 1):
#     while counter_j in range(num_vertices + 1):
#         min_counter = min(min_counter, value_compare(counter_i, counter_j, num_vertices))
#         counter_j += 1
#         print(counter_i, counter_j)
#     counter_j = 1
#     counter_i += 1

# for x in value_store:
#     for values in value_store[x][x].values():
#         if values < 0:
#             print("Negative cycle")
#
# print(min_counter)
# print(value_store)
