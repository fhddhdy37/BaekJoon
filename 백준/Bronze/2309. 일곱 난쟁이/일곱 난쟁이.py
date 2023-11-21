import copy

def combination(arr):
    newArr = copy.deepcopy(arr)
    
    for i in range(0, 8):
        for j in range(i+1, 9):
            newArr.pop(j)
            newArr.pop(i)
            if sum(newArr) == 100:
                return sorted(newArr)
            newArr = copy.deepcopy(arr)

H = []
arr = []

for i in range(9):
    H.append(int(input()))

arr = combination(H)

for n in arr:
    print(n)