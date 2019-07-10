knapsack_size = 0
number_of_items = 0

items_list = []

# Read input in
file = open("HW4_Part1_Data.txt", "r")
data = file.readlines()

for line in data[:1]:
    knapsack_size, number_of_items = map(int, line.strip('\n').split())

for line in data[1:]:
    items_list.append(list(map(int, line.strip('\n').split())))

A = [[0 for e in range(knapsack_size + 1)] for f in range(number_of_items + 1)]

for y in range(1, number_of_items + 1, 1):
    for z in range(knapsack_size + 1):
        if items_list[y-1][1] > z:
            A[y][z] = A[y-1][z]
        else:
            A[y][z] = max(A[y - 1][z], A[y - 1][z - items_list[y-1][1]] + items_list[y-1][0])

print(A[number_of_items][knapsack_size])
# Part 1: 2493893
