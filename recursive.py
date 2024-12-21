def merge_sorted_recursive(arr1, arr2):
    # Base cases
    if not arr1:  # Jika arr1 kosong, kembalikan arr2
        return arr2
    if not arr2:  # Jika arr2 kosong, kembalikan arr1
        return arr1
    
    # Bandingkan elemen pertama dari kedua array dan gabungkan secara rekursif
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge_sorted_recursive(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge_sorted_recursive(arr1, arr2[1:])

# Driver code
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = merge_sorted_recursive(arr1, arr2)

for value in arr3:
    print(value, end=" ")
