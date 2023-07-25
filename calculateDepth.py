class Node:
    def __init__(self):
        self.right = None
        self.left = None

def calculateMaxDepth(n):
    if n is None:
        return 0
    
    left_depth = calculateMaxDepth(n.left)
    right_depth = calculateMaxDepth(n.right)
    
    return max(left_depth, right_depth) + 1

# Membuat pohon biner seperti pada contoh
root = Node()
root.left = Node()
root.right = Node()
root.left.right = Node()

# Menghitung kedalaman maksimum
max_depth = calculateMaxDepth(root)

# Menampilkan hasil
print("Kedalaman maksimum dari pohon biner adalah:", max_depth)
