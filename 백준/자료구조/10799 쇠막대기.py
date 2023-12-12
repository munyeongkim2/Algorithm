ring = input()
stack = []
answer = 0
# stack.append(ring[0])
for i in range(len(ring)):
    if ring[i] == '(':
        stack.append('(')

    else:
        if ring[i - 1] == '(':
            stack.pop()
            answer += len(stack)

        else:
            stack.pop()
            answer += 1

print(answer)

#)이 나오면 2가지로 나눠야 함
# 1. 이전문자가 ( 면 레이저 니깐 스택에 쌓인 갯수 더함
# 2. 이전문자가 ) 면 쇠막대기 끄뜨멀이임. 하나씩만 추가해주기
