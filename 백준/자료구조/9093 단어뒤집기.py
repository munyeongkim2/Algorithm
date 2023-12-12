import sys

rang= int(sys.stdin.readline())

for i in range(rang):
    ans = []
    sen = sys.stdin.readline().split()
    for i in sen:
        ans.append(i[::-1])
    print(' '.join(ans))