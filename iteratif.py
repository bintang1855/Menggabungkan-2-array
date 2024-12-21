def merge_sorted_iterative(arr1, arr2):
    # Hasil array yang akan diisi
    merged = []
    i, j = 0, 0

    # Loop hingga salah satu array habis
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Menambahkan elemen yang tersisa dari array pertama
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Menambahkan elemen yang tersisa dari array kedua
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Driver code
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = merge_sorted_iterative(arr1, arr2)

for value in arr3:
    print(value, end=" ")
