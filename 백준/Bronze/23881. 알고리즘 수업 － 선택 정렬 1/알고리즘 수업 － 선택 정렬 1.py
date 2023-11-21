N, K = map(int, input().split())
A = list(map(int, input().split()))
maxNum = 0
count = 0
temp = 0

for i in range(N, 1, -1):
    maxNum = max(A[:i])
    if A[i-1] != maxNum:
        temp = A[i-1]
        A[i-1] = maxNum
        A[A.index(maxNum)] = temp
        count += 1
    if count == K:
        print(temp, maxNum)

if count < K:
    print(-1)