def stop_it(cur, end=45):
    return cur >= end


n = int(input())
a = [[0]*n for i in range(n)]
stop = n**2
gen_n = (x for x in range(1, stop+1))
m = 0
i, j = 0, 0
flag = 0
while True:
    for j in range(m, len(a)-m):
        a[i][j] = next(gen_n)
        if stop_it(a[i][j], stop):
            flag = 1
            break
    if flag:
        break
    for i in range(m+1, len(a)-m):
        a[i][j] = next(gen_n)
        if stop_it(a[i][j], stop):
            flag = 1
            break
    if flag:
        break
    for j in range(len(a)-m-2, m-1, -1):
        a[i][j] = next(gen_n)
        if stop_it(a[i][j], stop):
            flag = 1
            break
    if flag:
        break
    for i in range(len(a)-2-m, m, -1):
        a[i][j] = next(gen_n)
        if stop_it(a[i][j], stop):
            flag = 1
            break
    if flag:
        break
    m += 1

for row in a:
    print(*row)