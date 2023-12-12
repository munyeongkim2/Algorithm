import sys

ran= int(sys.stdin.readline())
ans = []
for i in range(ran):
    n = sys.stdin.readline().split()
    if n[0] == 'push':
        ans.append(n[1])
    elif n[0] == 'pop':
        if len(ans)==0:
            print(-1)
        else:
            print(ans.pop())
    elif n[0] == 'size':
        print(len(ans))
    elif n[0] =='empty':
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    elif n[0] =='top':
        if len(ans)==0:
            print(-1)
        else:
            print(ans[-1])