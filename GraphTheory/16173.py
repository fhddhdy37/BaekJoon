# 알고리즘은 푼것 같은데 채점은 틀렸다고 함
# 아마 입력받는것 때문 같은데 조건이 그지같아서 때려침

import random

def find_index(l, value):
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            if l[i][j] == value:
                return [i, j]
            

def find_path(l):
    jelly_location = find_index(l, jelly_str) # jelly_list에서 젤리의 위치를 좌표로 찾아냄
    jelly_num = game_board[jelly_location[0]][jelly_location[1]] # game_board에서 젤리의 위치의 숫자
    
    if jelly_num == -1: # 도착했을 때
        return print("HaruHaru")
    
    try:
        if jelly_location[1] + jelly_num >= input_n: # 현재 위치에서 오른쪽으로 갈수 없을 때
            jelly_list[jelly_location[0]][jelly_location[1]] = None
            jelly_location = [jelly_location[0] + jelly_num, jelly_location[1]]
            jelly_list[jelly_location[0]][jelly_location[1]] = jelly_str

            find_path(l)
        else:                                        # 현재 위치에서 오른쪽으로 갈수 있을 때
            jelly_list[jelly_location[0]][jelly_location[1]] = None
            jelly_location = [jelly_location[0], jelly_location[1] + jelly_num]
            jelly_list[jelly_location[0]][jelly_location[1]] = jelly_str

            find_path(l)
            
    except IndexError: # 구역 밖으로 나갈 때
        return print("Hing")
    

input_n = int(input())
input_line = ''
input_line_split = []

game_board = []
jelly_str = '쩰리'
jelly_list = [] # game_board에서 쩰리의 위치를 리스트로 표현
jelly_location = [] # game_board에서 쩰리의 위치를 좌표로 표현
jelly_num = 0

if input_n >= 2 and input_n <= 3:

    for i in range(0, input_n):
        input_line = input()
        input_line_split = input_line.split(' ')
        game_board.append(list())
        for j in range(0, input_n):
            if int(input_line_split[j]) >= 0 and int(input_line_split[j]) <= 100:
                game_board[i].append(int(input_line_split[j]))
    
    game_board[-1][-1] = -1

    for i in range(0, len(game_board)):
        jelly_list.append(list())
        for j in range(len(game_board[i])):
            jelly_list[i].append(None)

    jelly_list[0][0] = jelly_str

    find_path(jelly_list)