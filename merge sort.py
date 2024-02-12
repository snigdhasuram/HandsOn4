
def mergeSort(A):
    if len(A) > 1:
        middle = len(A) // 2
        left = A[:middle]
        right = A[middle:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              A[k] = left[i]
              i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k]=right[j]
            j += 1
            k += 1
    return A

K = int(input("K: "))
N = int(input("N: "))
array=[]
for i in range(K):
    array+=list(map(int,input("array%d: "%(i+1)).split(",")))
print("Output: ",mergeSort(array))
