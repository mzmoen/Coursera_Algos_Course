from statistics import median

sum = 0

def QuickSort(A, n):
    if n==1:
        return A
    else:
        p = 0
        pivot_number = A[p]
        # pivot_number = [A[0], A[n-1], A[int((n+1)/2)-1]]
        # pivot_median = median(pivot_number)
        # p = A.index(pivot_median)
        if p != 0:
            Swap(A, p, 0)
        global sum
        sum += n-1
        A, i = Partition(A,0,n)
        A_part1 = QuickSort(A[:max(i - 1, 1)], len(A[:max(i - 1, 1)]))
        A_part2 = QuickSort(A[min(i, n-1):], len(A[min(i, n-1):]))
        print(A_part1 + [pivot_number] + A_part2, pivot_number, n)
        if max(A) == pivot_number or min(A) == pivot_number:
            return A_part1 + A_part2
        else:
            return A_part1 + [pivot_number] + A_part2




def Swap(A, l, r):
    A[l], A[r] = A[r], A[l]
    return A

def Partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l+1, r):
        if A[j] < p:
            Swap(A, j, i)
            i += 1
    Swap(A, l, i-1)
    # if l + 1 < i - 1:
    #     Partition(A, l, i-1)
    # if i+1 < r-1:
    #     Partition(A, i, r)
    return A, i

def read_file():
    file = open("HW_3_TextFile.txt", "r")
    int_array = []
    for line in file:
        int_array.append(int(line.strip('\n')))
    return int_array

# array = [3,8,2,5,1,4,7,6]
array = [1, 6, 8, 10, 7, 5, 2, 9, 4, 3]
# array = [4,3,2,5,1]
# array = [11,18,5,20,8,10,3,2,17,4,13,7,12,9,6,16,19,15,1,14]

#first is 162085, second is 164123, third is 138382

# array = read_file()

print(QuickSort(array, len(array)))

print("Final Sum:", sum)
