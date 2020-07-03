def checkprime(n):
    c=0
    for i in range(1,n+1):
        if n % i==0:
            c=c+1
    if c==2:
        print(bool(1))
    else:
        print(bool(0))

checkprime(12)
checkprime(23)