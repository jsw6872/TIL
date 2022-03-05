number = int(input())
time = list(map(int, input().split()))

time.sort()

answer = 0
for i in range(1, number+1):
    answer += sum(time[:i])

print(answer)
