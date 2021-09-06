import math

def is_leap(year):
    leap = False
    factors = []
    
    #The year can be evenly divided by 4, is a leap year, unless:
    '''
    for whole_number in range(1, int(math.sqrt(year)) + 1):
        if year % whole_number == 0:
            factors.append(whole_number)
    print(math.sqrt(year))
    print (factors)
    '''
    
    if (year%4==0):
        leap=True
        if (year%100==0):
            leap=False
            if (year%400==0):
                leap=True
    #The year can be evenly divided by 100, it is NOT a leap year, unless:
    #The year is also evenly divisible by 400. Then it is a leap year.
    
    return leap
    


year = int(input())
print(is_leap(year))



