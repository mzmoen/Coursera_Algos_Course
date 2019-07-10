length = 0
verteces = [0]
A = [0]
answer_verteces = [1, 2, 3, 4, 17, 117, 517, 997]

# Read input in
file = open("HW3_Part3_Data.txt", "r")
data = file.readlines()

for line in data[:1]:
    length = int(line.strip('\n'))

for line in data[1:]:
    verteces.append(int(line.strip('\n')))

A.append(verteces[1])

for enum, x in enumerate(verteces[2:]):
    A.append(max(A[enum + 1], A[enum] + verteces[enum + 2]))

S = []
i = len(A)

while i >= 1:
    if A[i-2] >= A[i-3] + verteces[i-1]:
        i -= 1
    else:
        S.append(i-1)
        if i-1 in answer_verteces:
            print(i-1)
        i -= 2


