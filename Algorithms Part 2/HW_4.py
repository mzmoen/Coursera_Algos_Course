int_dict = {}

#####################
# Read input in
file = open("HW_4_Data.txt", "r")
data = file.readlines()

for line in data:
    int_dict[int(line.strip('\n'))] = 1


####################
# Count target matches
def count_match(dictionary, target):
    counter = 0
    for x, y in dictionary.items():
        if target - x in dictionary and x != target - x:
            counter += 1
            # print(x, target - x, target)
            break
    return counter


###################
# Create target list
target_list = list(range(-10000, 10001))


###################
# Print number of matches
overall_counter = 0
for x in target_list:
    overall_counter += count_match(int_dict, x)

print(overall_counter)

########
# Test1 t = [3,10], answer = 8




