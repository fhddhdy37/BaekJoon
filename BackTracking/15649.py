
def permutation(N, M):
    global count
    global c
    
        
    print(b)
    f = b.pop(count)
    
    if count == 1:
        c = [] + [f]
    else:
        c = c + [f]
        
    #print(c)
    permutation(N, M)
    
    
    b.insert(count, f)
        
    
    # for i in range(0, len(b)):
    #     f = b.pop(i)
    #     c = [] + [f]
    
    #     for j in range(0, len(b)):
    #         e = b.pop(j)
    #         d = c + [e]
    #         print(d)

    #         b.insert(j, e)
        
    #     b.insert(i, f)
    
    if count >= M:
        return
    else:
        count += 1
        

a = input("input : ")
b = []

N = int(a.split(' ')[0])
M = int(a.split(' ')[1])

for i in range(0, N):
    b.append(i + 1)
    

c = []
d = []


count = 0
permutation(N, M)

    
    