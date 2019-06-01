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
            bubble_down_location = 0
            while heap_max[bubble_down_location] > min(heap_max[bubble_down_location * 2 + 1], heap_max[bubble_down_location * 2 + 2]):
                swap_location = heap_max.index(min(heap_max[bubble_down_location * 2 + 1], heap_max[bubble_down_location * 2 + 2]))
                heap_max[bubble_down_location], heap_max[swap_location] = heap_max[swap_location], heap_max[bubble_down_location]
                bubble_down_location = swap_location
                if (swap_location * 2 + 2) >= len(heap_max):
                    break

        else:
            heap_max.append(heap_min.pop(0) * (-1))
            reorder_heap(heap_max)
            heap_min.insert(0, heap_min.pop(len(heap_min) - 1))
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

    if counter_k % 2 == 0:
        median_list.append(heap_min[0]*(-1))
    else:
        if len(heap_max) > len(heap_min):
            median_list.append(heap_max[0])
        else:
            median_list.append(heap_min[0]*(-1))


sums = sum(median_list)
print(sums % 10000)