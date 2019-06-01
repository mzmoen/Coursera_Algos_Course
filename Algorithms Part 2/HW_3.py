##########
median_list = []
heap_min = []
heap_max = []
counter_k = 0


##########
def reorder_heap(heap_list):
    heap_length = len(heap_list)
    new_element_location = heap_length-1
    parent_location = new_element_location // 2 - ((new_element_location + 1) % 2)
    while heap_list[new_element_location] < heap_list[parent_location]:
        heap_list[new_element_location], heap_list[parent_location] = heap_list[parent_location], \
                                                                                 heap_list[new_element_location]
        new_element_location = parent_location
        if new_element_location == 0:
            break
        parent_location = new_element_location // 2 - (new_element_location + 1) % 2
    return heap_list


##########
median_list.append(0)

file = open("HW_3_Data.txt", "r")
data = file.readlines()

for line in data:
    line = line.strip()
    counter_k += 1
    if int(line) <= median_list[counter_k - 1]:
        heap_min.append(int(line)*(-1))
        heap_min = reorder_heap(heap_min)
    else:
        heap_max.append(int(line))
        heap_max = reorder_heap(heap_max)

    if abs(len(heap_max) - len(heap_min)) > 1:
        if len(heap_max) > len(heap_min):
            heap_min.append(heap_max.pop(0) * (-1))
            reorder_heap(heap_min)
            heap_max.insert(0, heap_max.pop(len(heap_max) - 1))
            # if heap_max[0] > heap_max[1]:
            #     heap_max[0], heap_max[1] = heap_max[1], heap_max[0]
            bubble_down_location = 0
            while heap_max[bubble_down_location] > min(heap_max[bubble_down_location * 2 + 1], heap_max[bubble_down_location * 2 + 2]):
                swap_location = heap_max.index(min(heap_max[bubble_down_location * 2 + 1], heap_max[bubble_down_location * 2 + 2]))
                heap_max[bubble_down_location], heap_max[swap_location] = heap_max[swap_location], heap_max[bubble_down_location]
                bubble_down_location = swap_location
                if (swap_location * 2 + 2) >= len(heap_max):
                    break


            # swap_value = heap_max[0]
            # while heap_max.index(swap_value) != (len(heap_max) - 1):
            #     current_location = heap_max.index(swap_value)
            #     if current_location * 2 + 2 >= len(heap_max):
            #         break
            #     swap_location = heap_max.index(
            #         min(heap_max[current_location * 2 + 1], heap_max[current_location * 2 + 2]))
            #     heap_max[current_location], heap_max[swap_location] = heap_max[swap_location], heap_max[
            #         current_location]
            # heap_min.append(heap_max.pop(heap_max.index(swap_value)) * (-1))
            # reorder_heap(heap_min)
        else:
            heap_max.append(heap_min.pop(0) * (-1))
            reorder_heap(heap_max)
            heap_min.insert(0, heap_min.pop(len(heap_min) - 1))
            # if heap_min[0] > heap_min[1]:
            #     heap_min[0], heap_min[1] = heap_min[1], heap_min[0]
            bubble_down_location = 0
            while heap_min[bubble_down_location] > min(heap_min[bubble_down_location * 2 + 1],
                                                       heap_min[bubble_down_location * 2 + 2]):
                swap_location = heap_min.index(
                    min(heap_min[bubble_down_location * 2 + 1], heap_min[bubble_down_location * 2 + 2]))
                heap_min[bubble_down_location], heap_min[swap_location] = heap_min[swap_location], heap_min[
                    bubble_down_location]
                bubble_down_location = swap_location
                if (swap_location * 2 + 2) >= len(heap_min):
                    break
            # swap_value = heap_min[0]
            # while heap_min.index(swap_value) != (len(heap_min) - 1):
            #     current_location = heap_min.index(swap_value)
            #     if current_location * 2 + 2 >= len(heap_min):
            #         break
            #     swap_location = heap_min.index(min(heap_min[current_location * 2 + 1], heap_min[current_location * 2 + 2]))
            #     heap_min[current_location], heap_min[swap_location] = heap_min[swap_location], heap_min[current_location]
            # heap_max.append(heap_min.pop(heap_min.index(swap_value)) * (-1))
            # reorder_heap(heap_max)

    if counter_k % 2 == 0:
        median_list.append(heap_min[0]*(-1))
    else:
        if len(heap_max) > len(heap_min):
            median_list.append(heap_max[0])
        else:
            median_list.append(heap_min[0]*(-1))
    # if counter_k > 10:
    #     print(min(heap_min), heap_min[0], min(heap_max), heap_max[0], median_list[len(median_list)-1], line)
    # if counter_k == 100:
    #     break


# print(median_list)
# print(heap_max)
sums = sum(median_list)
print(sums % 10000)

# Test 1 input:
# 1
# 666
# 10
# 667
# 100
# 2
# 3
#
# Output (sum of medians modulo 10000):
# 142
#
# Test 2 input:
# 6331
# 2793
# 1640
# 9290
# 225
# 625
# 6195
# 2303
# 5685
# 1354
#
# Output (sum of medians modulo 10000):
# 9335