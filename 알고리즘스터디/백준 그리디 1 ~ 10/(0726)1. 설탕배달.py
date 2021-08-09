
N = int(input())
num = 0 
if N == 1 or N == 2 or N == 4 or N==7:
    print(-1)
else:
    for i in range(1000):
        if ( N - 5*i ) % 3 == 0 and N >= 5*i:
            num = i + ((N-5*i)//3)
    print(num)
            