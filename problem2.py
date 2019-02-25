'''
This problem was asked by Uber.

Given an array of integers, 
return a new array such that each element at index i of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def multip_array_element(array):
    cursor = 0
    new_array = []
    # initial result of multiply all elements of array, with help of cursor, we can except this index of out array
    mul_elem = 1
    # idea is set value of current index egale 1 to ignore this impact on calculation multiply
    array_copy = array.copy()
    while cursor < len(array):
        # absorption of multiply
        array_copy[cursor] = 1

        for e in array_copy:
            mul_elem *= e

        new_array.append(mul_elem)

        # for a new loop we need to initiate array and mul_elem, incremente cursor
        array_copy = array.copy()
        cursor += 1
        mul_elem = 1
    # show the new array as a result
    print(new_array)

    # this function have O(N^2) complexity
    
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    multip_array_element(array)
    array = [3, 2, 1]
    multip_array_element(array)