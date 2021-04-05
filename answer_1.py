### Inputs
start = [900,940,950,1000,1500,1600]
stop = [910,1020,1010,1015,1620,1700]
n = 6

### Function return the minimum number of processes required
def findProcessors(start,stop,n):
    
    if n == 0:
        return 0 
    
    elif n == 1:
        return 1
    
    else:
        p = 1
        for i in range(len(start)):
            cnt = 1
            for j in range(len(start)- i - 1):
                if stop[i] >= start[len(start)-j-1]:
                    cnt = cnt + 1
            if cnt > p:
                p = cnt
        return p


print(findProcessors(start,stop,n))