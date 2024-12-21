def merge_sorted_recursive(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge_sorted_recursive(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge_sorted_recursive(arr1, arr2[1:])

# Input dinamis
arr1 = list(map(int, input("Masukkan elemen array pertama (pisahkan dengan spasi): ").split()))
arr2 = list(map(int, input("Masukkan elemen array kedua (pisahkan dengan spasi): ").split()))

# Memastikan array diurutkan
arr1.sort()
arr2.sort()

# Memanggil fungsi
result = merge_sorted_recursive(arr1, arr2)
print("Array yang digabung dan diurutkan (Rekursif):", result)
