# 메모리 최적화 실패
# 재귀 돌리는 중에 메모리가 터짐

def levelBurger(N):
    burger = ''
    
    if N == 0:
        burger = patty
        return burger
    elif N >= 1 and N <= 50:
        lvBurgerN1 = levelBurger(N - 1)
        burger = bun + lvBurgerN1 + patty + lvBurgerN1 + bun
        return burger

a = input()
N = int(a.split(' ')[0])
X = int(a.split(' ')[1])
countPatty = 0
patty = 'P'
bun = 'B'

lvBurger = levelBurger(N)[0 : X]

if X >= 1 and X <= len(lvBurger):
    countPatty = lvBurger.count('P')
    
print(lvBurger)
print(countPatty)
