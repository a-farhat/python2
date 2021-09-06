
calclist= []
ops = [5,2,"C","D","+"]
sum = 0
for i in ops:
    print(calclist)
    if type(i)==str:
        print ('this is a string')
        if i=="C":
            if(len(calclist)>0):
                calclist.pop()
        elif i=="D":
            if(len(calclist)>0):
                listitem = calclist.pop()
                i=2*listitem
                calclist.append(listitem)
                calclist.append(i)
        elif i=="+":
            if(len(calclist)>0):
                item1=calclist.pop()
                item2=calclist.pop()
                calclist.append(item1)
                calclist.append(item2)
                calclist.append(item1+item2)
    elif type(i)==int:
        calclist.append(i)

for x in calclist:
    sum = sum + x

print(sum)
    
    



#def greetings_function(name ):
#    print ('Welcome ' + name + ' from the function')


#greetings_function('Ahmad')


#def tuple_param(*names):
#    print('Welcome all ' + str(names))


#def add_numbers(num1,num2):  
#    return num1+num2

#num1=int(input('Enter the first number: '))
#num2=int(input('Enter the second number: '))
#print(add_numbers(num1,num2))



#print('Hello')
#tuple_param('one','two')

#pets = ['dog',1, '+' ,'C', True, 'snake']
#pets2 = list(('dog',1, '+' ,'C', True, 'snake'))

#print (pets)

#print (pets2)s