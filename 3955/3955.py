import sys
input = sys.stdin.readline

def eea(n, m):
    r1, r2 = m, n
    t2 = -~(t1 := 0)
    while r2:
        s = r1 // r2
        r = r1 - s * r2
        r1, r2 = r2, r
        t = t1 - s * t2
        t1, t2 = t2, t

    return 0 if r1 != 1 else (m + t1) % m

for _ in range(int(input())):
    k, c = map(int, input().split())
    if c == 1:
        print(-~k if k < 10**9 else 'IMPOSSIBLE')
        continue
    if k == 1:
        print(1)
        continue
    p = eea(c, k)
    if p > 10**9 or not p:
        print('IMPOSSIBLE')
    else:
        print(p)
    
    
