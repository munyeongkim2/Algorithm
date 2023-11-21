import sys

none = False
ans = []
reans = []

sen = list(sys.stdin.readline().rstrip())
for i in sen:
    if '<' == i:
        if len(reans) != 0:
            ans.extend(reversed(reans))
            reans.clear()
        ans.append("<")
        none = True
    elif '>' == i:
            ans.append(">")
            none = False
    
    elif none == False:
        if i == ' ':
            if len(reans) == 0:
                ans.append(' ')
            else:
                ans.extend(reversed(reans))
                ans.append(' ')
                reans.clear()
        else:
         reans.append(i)
    else:
            ans.append(i)

if len(reans) != 0:
    ans.extend(reversed(reans))

print(''.join(ans))

