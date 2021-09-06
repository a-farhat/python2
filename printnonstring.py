
if __name__ == '__main__':
    n = int(input())
    values=[]
    for i in range(1,n+1):
        values.append(i)
    
    print(*values, sep='', end='\n')