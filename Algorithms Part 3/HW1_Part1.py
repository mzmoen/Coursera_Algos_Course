from operator import itemgetter

list_jobs = []

#####################
# Read input in
file = open("HW1_Part1_Data.txt", "r")
data = file.readlines()
x = 0

for line in data:
    list_jobs.append(list(map(int, line.strip('\n').split())))
    if x > 0:
        # order by difference: answer = 69119377652
        list_jobs[x].append(list_jobs[x][0] - list_jobs[x][1])
        # order by ratio: answer = 67311454237
        # list_jobs[x].append(list_jobs[x][0] / list_jobs[x][1])
    x += 1

sorted_jobs = sorted(list_jobs[1:], key=itemgetter(2, 0), reverse=True)
print(sorted_jobs)

length = 0
weighted_sum = 0
for x in sorted_jobs:
    length += x[1]
    weighted_sum += x[0] * length

print(weighted_sum)
