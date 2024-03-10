x={'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
  'Marina': '8877-7788'}
x ['Luan']= '8878-9986'
print(x.values())
for i in x:
    if x[i] =='1234-5678':
        print(i)
        break
    else:
        print('Não existe')

#//////////////////////////////////////////////////////////////////////////////////////////////////////

def sauda(nome):
    print('ola ',nome,)
    sauda2(nome)
    print('preparado para dizer tchau ?')
    tchau()

def sauda2(nome):
    print('Como vai ? ',nome)

def tchau():
    print('Adeus')


sauda('Yago')

def fat(x):
    if x == 1:
        return 1
    elif x != 1:
        return (x*fat(x-1))



print(fat(6))

def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

x = [1,2,12,4,5,9,7,8,72]
print(count(x))

def binary_search(arr, target):
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid+1:], target)


print(binary_search([6, 7, 8, 9, 10], 8))
print(binary_search([6, 7, 8, 9, 10], 6))

def find_max(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

print(sum_array(x))
print(find_max(x))

def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(x))
print([i for i in x[0:]])
print([i for i in x[:6] if i >=5])
y =[7,2,5,9,45,6,79,3,2,26,78,98]
print(quicksort(y))

