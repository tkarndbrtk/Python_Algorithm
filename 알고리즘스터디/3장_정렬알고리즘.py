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
# 퀵정렬
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x> pivot]

    return quick(left_side) + [pivot] + quick(right_side)

print(quick(array))
'''
# 계수정렬
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] *(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
'''

# Quiz

A =[5,3,2,6,1]
B =[8,1,5,9,4]
K = 3

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))
