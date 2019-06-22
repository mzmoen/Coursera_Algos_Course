k = 4
edges = []
clusters_hash = {}

for i in range(501):
    clusters_hash[i] = i

#####################
# Read input in
file = open("HW2_Part1_Data.txt", "r")
data = file.readlines()[1:]

for line in data:
    edges.append(list(map(int, line.strip('\n').split())))

edges = sorted(edges, key=lambda z: z[2])

for x in edges:
    if clusters_hash[x[0]] == clusters_hash[x[1]]:
        continue
    elif len(set(clusters_hash.values())) <= k+1:
        print(x[2])
        break
    else:
        cluster_to_move = clusters_hash[x[0]]
        clusters_hash[x[0]] = clusters_hash[x[1]]
        for key, value in clusters_hash.items():
            if value == cluster_to_move:
                clusters_hash[key] = clusters_hash[x[1]]
