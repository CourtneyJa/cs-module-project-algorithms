'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    l = len(arr)
    if l < 2:
        return arr
    i= 0
    n = 1
    while n < l:
        if arr[i] == 0:
            if arr[n] == 0:
                n += 1
            else:
                arr[i] = arr[n]
                arr[n] = 0
        else:
            i += 1
            n += 1
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")