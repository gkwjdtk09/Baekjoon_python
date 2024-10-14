A, B = map(int,input().split())
C = int(input())
if (B+C)> 59 :
    A += (B+C)/60
    if(A>=24):
        A -= 24
    print(int(A), (B+C)%60)
else :
    print(A, (B+C))