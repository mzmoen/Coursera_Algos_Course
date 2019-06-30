from networkx.utils.union_find import UnionFind
import copy

nodes = []
nodes_dic = {}


def hamming_distance(a, b, range_def):
    hamming_dist = 0
    for x in range(range_def):
        hamming_dist += a[x] ^ b[x]
    return hamming_dist


# Read input in
file = open("HW2_Part2_Data.txt", "r")
data = file.readlines()[1:]

for line in data:
    key = tuple(map(int, line.strip('\n').split()))
    nodes.append(key)
    nodes_dic[''.join(map(str, key))] = 1

set_nodes = set(sorted(nodes, key=lambda z: sum(z)))

union_find = UnionFind(set_nodes)
# print(nodes_dic)

for x in union_find:
    iter_count1 = 0
    for y in x:
        new_code = list(x)
        new_code[iter_count1] = abs(y - 1)
        if ''.join(map(str, new_code)) in nodes_dic:
            union_find.union(x, tuple(new_code))
        iter_count2 = iter_count1 + 1
        for z in x[iter_count2:]:
            new_code2 = copy.deepcopy(new_code)
            new_code2[iter_count2] = abs(z - 1)
            if ''.join(map(str, new_code2)) in nodes_dic:
                union_find.union(x, tuple(new_code2))
            iter_count2 += 1
        iter_count1 += 1

pointer_set = set([union_find[x] for x in set_nodes])
print(len(pointer_set))

#6118


# for x in union_find:
#     for y in union_find:
#         if union_find[x] != union_find[y]:
#             if hamming_distance(x, y, len(x)) < 3:
#                 union_find.union(x, y)
#
#
# pointer_set = set([union_find[x] for x in set_nodes])
# print(len(pointer_set))
