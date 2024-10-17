more = True

while more:
    A, B = map(int,input().split())
    if A == B == 0:
        more = False
    else: print(A+B)