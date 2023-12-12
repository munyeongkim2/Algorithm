import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
ans = deque(list(range(1,n+1)))
yo = []
count = 0
while len(ans) != 0:
        i = ans.popleft()
        count += 1
        if count % k != 0:
            ans.append(i)
        else:
            yo.append(i)

print(f"<{', '.join(map(str,yo))}>")
