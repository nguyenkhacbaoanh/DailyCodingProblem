'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def find_target(array, target):
    # array_sorted = sorted(array)
    i = 0
    j = len(array) - 1
    result = False
    while i < len(array) and j >=0:
        value1 = array[i]
        value2 = array[j]
        r = value1 + value2
        if r == k:
            result = True
            break
        i += 1
        j -= 1

    return result
    # this function have O(N) complexity


if __name__ == "__main__":
    array = [10,15,3,7]
    k = 17
    print(find_target(array, k))