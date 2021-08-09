# 선택정렬
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] >array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
'''
#삽입정렬
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i):
        if array[i] < array[j]:
            array.insert(j,array[i])
            array.pop(i+1)
            break
        

print(array)
'''