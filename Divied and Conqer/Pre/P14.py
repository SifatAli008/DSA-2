#PRINT NON-LEAVES
def print_non_leaves(bin, size, currNode):
    leftChild = 2 * currNode
    rightChild = 2 * currNode + 1

    if (leftChild >= size or bin[leftChild] == -1) and (rightChild >= size or bin[rightChild] == -1):
        return
    else:
        print(bin[currNode], end=" ")
        if leftChild < size and bin[leftChild] != -1:
            print_non_leaves(bin, size, leftChild)
        if rightChild < size and bin[rightChild] != -1:
            print_non_leaves(bin, size, rightChild)

bin = [-1, 10, 5, 18, 3, 7, 12, 20, -1, -1, 6, -1, -1, 15, 19, 21]
n = len(bin)

print_non_leaves(bin, n, 1)
