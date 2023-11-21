N, K = map(int, input().split())
A = list(map(int, input().split()))
maxNum = 0
count = 0
temp = 0
loc = 0
arr = []

for i in range(1, N):
    loc = i - 1
    temp = A[i]

    while 0 <= loc and temp < A[loc]:
        A[loc+1] = A[loc]
        loc -= 1
        count += 1
        if count == K:
            print(A[loc+1])
    if loc + 1 != i:
        A[loc+1] = temp
        count += 1
        if count == K:
            print(A[loc+1])

if count < K:
    print(-1)