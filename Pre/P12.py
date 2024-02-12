#sum of left Leaves

def sum_left_leaves(bin, size, currNode):
    leftChild = 2 * currNode
    rightChild = 2 * currNode + 1

    if (leftChild >= size or bin[leftChild] == -1) and (rightChild >= size or bin[rightChild] == -1):
        if currNode % 2 == 0:
            return bin[currNode]
        else:
            return 0
    else:
        total_sum = 0
        if leftChild < size and bin[leftChild] != -1:
            total_sum += sum_left_leaves(bin, size, leftChild)
        if rightChild < size and bin[rightChild] != -1:
            total_sum += sum_left_leaves(bin, size, rightChild)
        return total_sum

bin = [-1, 10, 5, 18, 3, 7, 12, 20, -1, -1, 6, -1, -1, 15, 19, 21]
n = len(bin)

print(sum_left_leaves(bin, n, 1))
