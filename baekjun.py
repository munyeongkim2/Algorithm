
import sys

# left = list(sys.stdin.readline().rstrip())
# right = []
ans = []
ran = int(sys.stdin.readline())

for i in range(ran):
    com =  list(map(str, sys.stdin.readline().split()))
    if com[0] == "push":
        ans.append(com[1])
    elif com[0]=="pop":
        if len(ans):
            print(ans[0])
            del ans[0]
        else:
            print(-1)
    elif com[0]=="size":
        print(len(ans))
    elif com[0]=="front":
        if len(ans):    
             print(ans[0])
        else:
            print(-1)  
    elif com[0]=="back":
        if len(ans):
            print(ans[-1])
        else:
            print(-1)
    else:
        if len(ans):
            print(0)
        else:
            print(1)
        


