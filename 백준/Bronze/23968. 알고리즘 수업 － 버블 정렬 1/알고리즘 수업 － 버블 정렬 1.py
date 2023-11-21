N, K = map(int, input().split())
A = list(map(int, input().split()))
maxNum = 0
count = 0
temp = 0
chk = True

for i in range(N, 0, -1):
    for j in range(N - 1):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            count += 1
        if count == K and chk:
            chk = False
            print(A[j], A[j+1])
            

if count < K:
    print(-1)
