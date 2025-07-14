
n,m = map(int,input().split())
dduk = list(map(int,input().split()))
#1
for i in range(m,max(dduk)):
    check = 0
    for j in dduk:
        d = j-i
        if d>0:
            check += d
    if check == m:
        print(i)
        break

#2
start = 0
end = max(dduk)

result = 0
while(start<=end):
    total = 0
    mid =(start+end)//2
    for x in dduk:
        if x> mid:
            total += x- mid
        if total <m:
            end = mid -1
        else:
            result = mid
            start =mid + 1
print(result)


#rewirte
start = 0
end = max(dduk)
while (start <= end):
    hap = 0
    mid = (start+end)//2
    for k in dduk:
        if k > mid:
            hap += k-mid
    if hap > m:
        start = mid+1
    elif hap < m:
        end = mid-1
    else:
        answer = mid
        start = mid+1
print(answer)
    