
def levelBurger(N):
    burger = ''
    patty = 'P'
    bun = 'B'
    if N == 0:
        burger = patty
        return burger
    elif N >= 1 and N <= 50:
        burger = bun + levelBurger(N - 1) + patty + levelBurger(N - 1) + bun
        return burger

a = input()
N = int(a.split(' ')[0])
X = int(a.split(' ')[1])
countPatty = 0

lvBurger = list(levelBurger(N))

if X >= 1 and X <= len(lvBurger):
    for i in range(0, X):
        if lvBurger.pop(0) == 'P':
            countPatty += 1
    
print(countPatty)
