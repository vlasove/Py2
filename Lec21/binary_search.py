def binarySerach(arr, x):
    low = 0 # индекс наименьший
    high = len(arr) - 1  # индекс наибольший

    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == x:
            return mid 
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [3,4,5,10,12,18,19,20,23]

ID = binarySerach(arr, 3)
print("Found id:", ID)
print("My element:", arr[ID])