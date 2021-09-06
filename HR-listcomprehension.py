if __name__ == '__main__':
    
    '''
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    '''
    x = 1
    y = 1
    z = 1
    n = 2

     #ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
    
    print([[a,b,c] for a in range(0,x+1)  for b in range(0,y+1) for c in range(0,z+1) if (a+b+c)!=n ] )
    
    