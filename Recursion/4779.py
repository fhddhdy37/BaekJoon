def cantor(num, a):
    if num < 3:
        return a
    else:
        a = list(a)
        b = ''

        for i in range(num // 3, num - num // 3):
            a[i] = ' '

        for i in range(0, len(a)):
            b += a[i]

        l1 = b[: num // 3]
        l2 = b[num // 3 : num - num // 3]
        l3 = b[num - num // 3 :]

        l1 = str(cantor(len(l1), l1))
        l3 = str(cantor(len(l3), l3))
        
        return l1 + l2 + l3

while True:
    try:
        N = int(input())

        num = 3 ** N
        a = num * "-"

        print(cantor(num, a))
    except ValueError:
        break
    except EOFError:
        break
