import itertools, copy

# Read input in
file = open("HW3_Part1_Data.txt", "r")
data = file.readlines()

city_location = []

for line in data[:1]:
    num_cities = int(line.strip('\n'))

for line in data[1:]:
    temp_city = list(map(float, line.strip('\n').split()))
    city_location.append(temp_city)

travel_path = []
stack = [city_location[0]]

def distance(a, b):
    return ((a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5

while stack:
    min_distance = 999999999999999
    min_travel_city = [999999999, 999999999, 9999999999, 99999999999]
    for city in [x for x in city_location[1:]]:
        travel_dist = distance(city, stack[0])
        if travel_dist < min_distance:
            if travel_dist == min_distance and city[0] > min_travel_city[0]:
                continue
            else:
                min_distance = distance(city, stack[0])
                min_travel_city = city
    city_location.remove(min_travel_city)
    min_travel_city.append(min_distance)
    travel_path.append(min_travel_city)
    stack.pop(0)
    print(min_travel_city)
    if len(city_location) != 1:
        stack.append(min_travel_city)
    else:
        city_location[0].append(distance(city_location[0], min_travel_city))
        travel_path.append(city_location[0])

print(travel_path)

total_distance_travelled = 0

for x in travel_path:
    total_distance_travelled += x[3]

print(total_distance_travelled)

# for idx, line in enumerate(data[1:]):
#     temp_city = list(map(float, line.strip('\n').split()))
#     print(idx)
#     if idx == 0:
#         city_location.append(temp_city)
#     elif idx == 1:
#         temp_city.insert(3, ((city_location[0][1] - temp_city[1]) ** 2 + (city_location[0][2] - temp_city[2]) ** 2) ** 0.5)
#         city_location.append(temp_city)
#     else:
#         for idy, y in enumerate(city_location):
#             distance = ((y[1] - temp_city[1]) ** 2 + (y[2] - temp_city[2]) ** 2) ** 0.5
#             if idy < len(city_location) - 1:
#                 if distance >= city_location[idy + 1][3]:
#                     continue
#                 else:
#                     temp_city.insert(3, distance)
#                     city_location.insert(idy + 1, temp_city)
#                     old_city = city_location[idy + 2]
#                     city_location[idy + 2][3] = ((temp_city[1] - old_city[1]) ** 2 + (temp_city[2] - old_city[2]) ** 2) ** 0.5
#                     break
#             else:
#                 temp_city.insert(3, distance)
#                 city_location.append(temp_city)
#                 break
#
# print(city_location)
#
# distance_sum = 0
#
# for x in city_location[1:]:
#     distance_sum += x[3]
#
# last_step = ((city_location[0][1] - city_location[len(city_location) - 1][1]) ** 2 + (city_location[0][2] - city_location[len(city_location) - 1][2]) ** 2) ** 0.5
#
# distance_sum += last_step
#
# print(distance_sum)

