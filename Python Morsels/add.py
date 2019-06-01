# def add(list1, list2):
#     combined_list = []
#     for x, i in enumerate(list1):
#         combined_list.append([])
#         for z in range(len(i)):
#             combined_list[x].append(i[z] + list2[x][z])
#     return combined_list


# def add_multiple_lists(*args):
#     combined_list = []
#     for x, i in enumerate(args[0]):
#         combined_list.append([])
#         for z in range(len(i)):
#             combined_list[x].append(0)
#             for a in range(len(args)):
#                 combined_list[x][z] += args[a][x][z]
#     return combined_list

def add(*args):
    combined_list = []
    args = sorted(args, key=lambda x: len(x))
    for x, i in enumerate(args[0]):
        combined_list.append([])
        for z in range(len(i)):
            combined_list[x].append(0)
            for a in range(len(args)):
                try:
                    combined_list[x][z] += args[a][x][z]
                except IndexError:
                    print("Given matrices are not the same size")
                    return None
    return combined_list


print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
