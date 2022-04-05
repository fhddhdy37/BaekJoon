def multipleOf3(num1):
    global count
    num2 = 0
    
    if len(num1) == 1:
        if int(num1) % 3 == 0:
            print(count)
            print("YES")
        else:
            print(count)
            print("NO")
    else:
        for i in range(0, len(num1)):
            num2 += int(num1[i])
            
        count += 1
        multipleOf3(str(num2))
        

num1 = input()
count = 0

if len(num1) <= 7 and int(num1) != 0:
    multipleOf3(num1)
