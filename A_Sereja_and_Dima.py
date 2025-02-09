n = int(input())
l = list (map(int,input().split()))
i , j = 0, len(l)-1
ser , dima = 0,0

while i<=j:
    if l[i]>l[j]:
        ser+=l[i]
        i+=1
        if i<=j and l[i]>l[j]:
            dima+=l[i]
            i+=1
        else:
            if i>j:
                break
            dima+=l[j]
            j-=1
    else:
        ser+=l[j]
        j-=1
        if i<=j and l[j]>l[i]:
            dima+=l[j]
            j-=1
        else:
            if i>j:
                break
            dima+=l[i]
            i+=1
print (ser, dima)
    

