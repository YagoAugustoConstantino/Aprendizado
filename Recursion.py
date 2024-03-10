def soma(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0]+ soma(arr[1:])

x = [1,2,3,5,7,8,9]

def count(arr):
    if len(arr) == 0 :
        return 0
    else:
        return 1 + count(arr[1:])

def maior(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:return arr[1]
    else:
        numero_maior=arr[0]
        if numero_maior < arr[1]:
            arr[1] = numero_maior
            return maior(arr[1:])
        else:
            return maior(arr[1:])

def binary_search(arr, target):
    if not arr:
        return -1

    low = 0
    high = len(arr)-1
    mid = (low + high) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)


print(count(x))
print(soma(x))
print(maior(x))
print(binary_search([1,2,3,5,7,8,9],5))