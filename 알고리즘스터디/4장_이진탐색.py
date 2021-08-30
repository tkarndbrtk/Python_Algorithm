# 이진 탐색 재귀문
'''
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) / 2

  if target == array[mid]:
    return mid
  if target > array[mid]:
    return binary_search(array,target, mid+1, end)
  if target < array[mid]:
    return binary_search(array, target, start, mid-1)

n, target = int(input().split())
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result = None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)
'''

# 떡 자르기
import sys
'''
num, hope = map(int,sys.stdin.readline().split())

rice = list(map(int, sys.stdin.readline().split()))
def rice_cake(num, hope, rice):
  max_height = max(rice)

  while 1:
    left_sum = 0
    for i in rice:
      left = i - max_height
      if left >=0:
        left_sum+=left
    if hope <= left_sum:
      return max_height
    else:
      max_height-=1

print(rice_cake(num, hope, rice))
'''
#----- 특정수 개수 구하기

import bisect
num, value = map(int,sys.stdin.readline().split())

x = list(map(int,sys.stdin.readline().split()))

right = bisect.bisect_right(x, value)
left = bisect.bisect_left(x, value)

if right-left ==0:
  print(-1)
else:
  print(right - left)
