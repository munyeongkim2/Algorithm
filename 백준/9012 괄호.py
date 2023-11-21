rang = int(input())
in_ = 0
out_ = 0
for i in range(rang):
    sen = list(input())
    if sen.count(')') == len(sen):
        print('NO')
        continue
    elif sen.count('(') == len(sen):
        print('NO')
        continue
    else:
        for i in range(len(sen)):
            sen = ''.join(sen)
            sen = sen.split('()')

        if ''.join(sen) == '' or ''.join(sen) == '()':
            print("YES")
        else:
            print("NO")