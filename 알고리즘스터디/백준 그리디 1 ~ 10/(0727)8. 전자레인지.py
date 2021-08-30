time_per_but = [300,60,10]
time = int(input())
button = []
for i in range(len(time_per_but)):
    button.append(time//time_per_but[i])
    time %= time_per_but[i]
if time ==0:
    print(*button)
else:
    print(-1) 
