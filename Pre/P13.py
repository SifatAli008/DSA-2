#Print Leaves

def print_leaves(bin, size, currNode):
    leftChild = 2 * currNode
    rightChild = 2 * currNode + 1

    if (leftChild >= size or bin[leftChild] == -1) and (rightChild >= size or bin[rightChild] == -1):
        print(bin[currNode], end=" ")
    else:
        if leftChild < size and bin[leftChild] != -1:
            print_leaves(bin, size, leftChild)
        if rightChild < size and bin[rightChild] != -1:
            print_leaves(bin, size, rightChild)

bin = [-1, 10, 5, 18, 3, 7, 12, 20, -1, -1, 6, -1, -1, 15, 19, 21]
n = len(bin)

print_leaves(bin, n, 1)
