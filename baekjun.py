# import sys

# sens = list(sys.stdin.readline())
# sens = sens[:-1]
# cur = len(sens)
# ran = int(input())

# for i in range(ran):
#     inpu = input().split(' ')
#     if inpu[0] == "L":
#         if cur != 0:
#             cur -= 1
#     elif inpu[0] == "D":
#         if cur != len(sens):
#             cur += 1
#     elif inpu[0] == "B":
#         if cur != 0:
#          del sens[cur-1]
#          cur -= 1

#     elif inpu[0] == "P":
#         sens.insert(cur,inpu[1])
#         cur += 1

            
# print(''.join(sens)) //시간초과


# 접근법은, 커서를 기준으로 문자열을 스택 두개에 나누어 담겠다는 것이다
#

import sys

left = list(sys.stdin.readline().rstrip())
right = []
ran = int(input())

for i in range(ran):
    inpu = list(sys.stdin.readline().split())
    if inpu[0] == "L":
        if len(left) != 0:
            right.append(left.pop())
            
    elif inpu[0] == "D":
        if len(right)!= 0:
            left.append(right.pop())
    elif inpu[0] == "B":
        if len(left) != 0:
            left.pop()

    elif inpu[0] == "P":
        left.append(inpu[1])

            
print(''.join(left)+''.join(reversed(right)))