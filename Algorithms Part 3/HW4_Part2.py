import sys

sys.setrecursionlimit(20000)

knapsack_size = 0
number_of_items = 0

items_list = []

# Read input in
file = open("HW4_Part2_Data.txt", "r")
data = file.readlines()

for line in data[:1]:
    knapsack_size, number_of_items = map(int, line.strip('\n').split())

for line in data[1:]:
    items_list.append(list(map(int, line.strip('\n').split())))

value_store = {}


def value_compare(i, x):
    if x not in value_store:
        value_store[x] = {}
    if x in value_store and i in value_store[x]:
        return value_store[x][i]
    elif i == 0:
        value_store[x][i] = 0
    elif items_list[i-1][1] > x:
        value_store[x][i] = value_compare(i - 1, x)
    else:
        value_store[x][i] = max(value_compare(i - 1, x), value_compare(i - 1, x - items_list[i-1][1]) + items_list[i-1][0])
    return value_store[x][i]


max_val = value_compare(number_of_items, knapsack_size)
print(max_val)


