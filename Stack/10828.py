#runtime err

def is_not_int(num_stack):
    if not num_stack:
        return False
    
    for i in num_stack:
        if type(i) == int:
            pass
        else:
            return False
    return True


num_stack = []
command = ''

input_N = int(input())

if input_N >= 1 and input_N <= 10000:
    for i in range(input_N):
        input_command = input()
        command = input_command.split(' ')[0]
        
        if command == 'push':
            num_stack.append(int(input_command.split(' ')[1]))
        elif command == 'pop':
            if is_not_int(num_stack):
                print(num_stack.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(num_stack))
        elif command == 'empty':
            if num_stack:
                print(0)
            else:
                print(1)
        elif command == 'top':
            if is_not_int(num_stack):
                print(num_stack[-1])
            else:
                print(-1)
                
                
        