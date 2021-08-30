num_people = int(input()) 
time_people = list(map(int,input().split()))
sum = 0
time_people.sort()
for i in range(len(time_people)):
    sum += time_people[i]*(len(time_people)-i)

print(sum)
