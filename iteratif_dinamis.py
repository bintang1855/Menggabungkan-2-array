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

# Input dinamis
arr1 = list(map(int, input("Masukkan elemen array pertama (pisahkan dengan spasi): ").split()))
arr2 = list(map(int, input("Masukkan elemen array kedua (pisahkan dengan spasi): ").split()))

# Memastikan array diurutkan
arr1.sort()
arr2.sort()

# Memanggil fungsi
result = merge_sorted_iterative(arr1, arr2)
print("Array yang digabung dan diurutkan (Iteratif):", result)
