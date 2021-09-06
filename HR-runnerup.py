if __name__ == '__main__':
    n = int(input())
    #n=5
    arr = map(int, input().split())
    revarr = []
    #arr=[2,3,6,6,5]
    #arr=map(int,[2,3,6,6,5])
    #arr.sort()
    maxn = 0
    runnerup = 0
    maxindex = 0
   
    l=list(arr) 
    maxn=l[0]
    for i in l:        
        revarr.append(i)
        if i>maxn:
            maxn = i
    
    revarr.sort()
    for j in reversed(revarr):              
        if len(revarr)==1:
            runnerup=j
        else: 
            if j<maxn:
                runnerup = j
                break
    
    

    
   
    print(runnerup)
                