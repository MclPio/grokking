arr = [3, 7, 8, 9, 11, 13]
val = 8

def search(arr, val, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return None
    
    mid = (low + high) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return search(arr, val, low, mid - 1)
    else:
        return search(arr, val, mid + 1, high)

print(search(arr, val))