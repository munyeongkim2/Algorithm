import sys
import collections

rang= int(sys.stdin.readline())
dq = collections.deque()

for i in range(rang):
    commend = sys.stdin.readline().rstrip().split()
    if commend[0] == "push_front":
        dq.appendleft(commend[1])
    elif commend[0] == "push_back":
        dq.append(commend[1])
    elif commend[0] == "pop_front":
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    elif commend[0] == "pop_back":
        if len(dq):
            print(dq.pop())
        else:
            print(-1)
    elif commend[0] == "size":
        print(len(dq))
    elif commend[0] == "front":
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    elif commend[0] == "back":
        if len(dq):
            print(dq[-1])
        else:
            print(-1)
    else:
        if len(dq):
            print(0)
        else:
            print(1)