class HuffNode:
    def __init__(self, idx, frequency, left_root = None, right_root = None):
        self.parent_idx = None
        self.idx = idx
        self.frequency = frequency
        self.left_root = left_root
        self.right_root = right_root
        self.character = ''

    def set_roots(self, left_root, right_root):
        self.left_root = left_root
        self.right_root = right_root

    def update_char(self, a):
        self.character = a + self.parent_idx.character

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f'HuffNode(idx: {self.idx}, freq: {self.frequency})'


id_counter = 0
node_length = 0

codes_2 = []

# Read input in
file = open("HW3_Part1_Data.txt", "r")
data = file.readlines()

for line in data[:1]:
    node_length = int(line.strip('\n'))

for line in data[1:]:
    # codes.append(int(line.strip('\n')))
    codes_2.insert(0, HuffNode(id_counter, int(line.strip('\n'))))
    id_counter += 1

codes_2.sort()
codes = codes_2

while len(codes_2) > 1:
    left_root = codes_2.pop(0)
    right_root = codes_2.pop(0)
    parent_node = HuffNode(id_counter, left_root.frequency + right_root.frequency, left_root, right_root)
    codes_2.insert(0, parent_node)
    left_root.parent_idx = parent_node
    right_root.parent_idx = parent_node
    codes_2.sort()
    id_counter += 1

print(codes_2)
print(codes_2[0].left_root.left_root.left_root.left_root, codes_2[0].right_root)
final_nodes = []

stack = [codes_2[0]]
while stack:
    root = stack.pop(0)
    if root.left_root is not None:
        root.left_root.character = '1' + root.character
        stack.append(root.left_root)
        if root.left_root.idx < node_length:
            final_nodes.append(root.left_root)
    if root.right_root is not None:
        root.right_root.character = '0' + root.character
        stack.append(root.right_root)
        if root.right_root.idx < node_length:
            final_nodes.append(root.right_root)

for x in final_nodes:
    print(x.character)

#19 and 9