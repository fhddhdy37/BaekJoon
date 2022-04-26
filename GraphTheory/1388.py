
import sys

def is_row(n, m):
    if m >= M:
        return False
    
    if n >= N:
        return True
    
    if tile[n][m] == '-':
        return True

    elif tile[n][m] == '|':
        return False
        
        
def find_tile(n, m):
    global count
    
    if n >= N:
        return
    
    if m >= M:
        m = 0
        find_tile(n + 1, m)
    
    if not check_tile[n][m]:
        check_tile[n][m] = True
        if is_row(n, m):
            if is_row(n, m) ^ is_row(n, m + 1): # 현재 위치와 다음 위치의 타일이 서로 다른 경우
                count += 1
        elif not is_row(n, m):
            if is_row(n, m) ^ is_row(n + 1, m):
                count += 1

        find_tile(n, m + 1)

sys.setrecursionlimit(10 ** 6)
        
input_n = input()

N = int(input_n.split(' ')[0])
M = int(input_n.split(' ')[1])

tile = []
input_tile = ''
check_tile = []
count = 0


for i in range(0, N):
    input_tile = input()
    tile.append(list())
    for j in range(0, M):
        tile[i].append(input_tile[j])
        
for i in range(0, N):
    check_tile.append(list())
    for j in range(0, M):
        check_tile[i].append(None)
    
find_tile(0, 0)
print(count)
