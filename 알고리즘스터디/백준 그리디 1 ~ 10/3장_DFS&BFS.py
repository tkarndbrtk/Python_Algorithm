def jegwi_func(i):
    if i ==100:
        return
    print(i, '번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    jegwi_func(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

def fac_jegwi(n):
    if n<=1:
        return 1
    return n * fac_jegwi(n-1)

def uclid(a, b):
    if a%b ==0:
        return b
    else:
        return uclid(b, a%b)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def a(i):
    if i == 1:
        return True
    print('ho')
    return False

print(a(1))