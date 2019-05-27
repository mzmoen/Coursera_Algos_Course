file = open("HW_3_Data.txt", "r")
data = file.readlines()

median_list = []
overall_list = []
x = 0

for line in data:
    x += 1
    line = line.strip()
    overall_list.append(int(line))
    overall_list.sort()
    median_list.append(overall_list[(len(overall_list) - 1) // 2])
    print(median_list[x - 1])
    if x == 4340:
        break

print(median_list)

sums = sum(median_list)
print(sums % 10000)
