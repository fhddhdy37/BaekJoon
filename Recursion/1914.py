# 시간초과

def hanoi(N, start, end, x):
    global count
    if N == 0:
        return
    
    if input_n >= 1 and input_n <= 20:
        if start is a:
            n1 = '1'
        elif start is b:
            n1 = '2'
        elif start is c:
            n1 = '3'

        if end is a:
            n2 = '1'
        elif end is b:
            n2 = '2'
        elif end is c:
            n2 = '3'
    
    hanoi(N - 1, start, x, end)
    end.append(start.pop())
    if input_n >= 1 and input_n <= 20:
        n3.append(n1 + ' ' + n2) 
    hanoi(N - 1, x, end, start)
    
    count += 1
    
input_n = int(input())
count = 0

a = []
b = []
c = []

n1 = ''
n2 = ''
n3 = []

for i in range(input_n, 0, -1):
    a.append(i)
    
hanoi(input_n, a, c, b)

print(count)

for line in n3:
    print(line)