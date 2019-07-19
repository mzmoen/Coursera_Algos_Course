import itertools, copy

# Read input in
file = open("HW2_Part1_Data.txt", "r")
data = file.readlines()

city_distances = {}
city_location = []
num_cities = 0

for line in data[:1]:
    num_cities = int(line.strip('\n'))

for idx, line in enumerate(data[1:14]):  # flip to [12:] when calcing second half
    city_location.append(list(map(float, line.strip('\n').split())))
    city_location[idx].insert(0, idx)
    city_distances[idx] = {}
    print(idx)
    if idx > 0:
        for idy, y in enumerate(city_location):
            distance = ((y[1] - city_location[idx][1]) ** 2 + (y[2] - city_location[idx][2]) ** 2) ** 0.5
            city_distances[idx][idy] = distance
            city_distances[idy][idx] = distance

city_distances[0][0] = 0

S = {}
S[(0,)] = {}
S[(0,)][0] = 0

for y in range(2, num_cities+1, 1):
    for x in itertools.combinations([x[0] for x in city_location], y):
        if 0 in x:
            S[x] = {}
            S[x][0] = 999999999999999
            for j in [a for a in x if a != 0]:
                S[x][j] = 999999999999999999
                for k in [b for b in x if b != j]:
                    temp_set = list(copy.deepcopy(x))
                    temp_set.remove(j)
                    temp_set = tuple(temp_set)
                    S[x][j] = min(S[x][j], S[temp_set][k] + city_distances[j][k])

min_distance = 999999999
# for x, y in S[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].items():
for x, y in S[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12].items():
    min_distance = min(min_distance, y + city_distances[0][x])


print(min_distance)

