# mem = O(n), t = O(n + n * 1 + d)
# n - len(array)
# d - depth of tree
def GenerateBBSTArray(a):
    array_size = len(a)
    result_tree = [None] * array_size

    sorted_array = sorted(a)

    generate_helper(result_tree, sorted_array, 0, 0, array_size -1)

    return result_tree

def generate_helper(accum_tree, array, parent_index, low, high):
    if low > high or parent_index >= len(array):
        return
    middle = (low + high) // 2
    accum_tree[parent_index] = array[middle]

    generate_helper(accum_tree, array, 2 * parent_index + 1, low, middle - 1)
    generate_helper(accum_tree, array, 2 * parent_index + 2, middle + 1, high)


    

