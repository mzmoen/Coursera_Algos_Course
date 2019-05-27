def sort_and_count(a, n):
    if n == 1:
        return (a, 0)
    else:
        mid_point = mid_split(n)
        first_half = a[:mid_point]
        second_half = a[mid_point:]
        # print(mid_point, first_half, second_half)
        (b, x) = sort_and_count(first_half, len(first_half))
        (c, y) = sort_and_count(second_half, len(second_half))
        # print(b, c, n)
        (d, z) = count_split_inv(b, c, n)

        return (d, x+y+z)


def mid_split(n):
    if n % 2 == 0:
        return  int(n/2)
    else:
        return int((n+1)/2)

def count_split_inv(b, c, n):
    i = 0
    j = 0
    d = []
    z = 0

    for k in range(n):
        if i >= len(b):
            d.insert(k, c[j])
            j += 1
            z += len(b) - i
            continue
        elif j >= len(c):
            d.insert(k, b[i])
            i += 1
            continue
        elif b[i] < c[j]:
            d.insert(k, b[i])
            i += 1
        else:
            d.insert(k, c[j])
            j += 1
            z += len(b) - i

    return (d, z)

def read_file():
    file = open("HW 2 Text File.txt", "r")
    int_array = []
    for line in file:
        int_array.append(int(line.strip('\n')))
    return int_array


# a = [1,2,3,4,5,6]
a = read_file()
print(sort_and_count(a, len(a)))