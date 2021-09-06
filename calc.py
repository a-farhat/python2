import mathMod


num1 = input('Enter the first number: ')

num2 = input ('Enter the second number: ')

operator = input('Enter + , - , / , *: ')


#def calculate(num1, num2, operator):
   
if operator == "+":
    #result = int(num1) + int(num2)
    #result = 'the addition is: ', num1+num2
    print('the addition is: ', mathMod.add(int(num1),int(num2)))
elif operator == "-":
    result = int(num1) - int(num2)
elif operator == "/":
    if(int(num2)>0):
        result = int(num1) / int(num2)
elif operator == "*":
    result = int(num1) * int(num2)

#return result



#print(calculate(num1,num2,operator))


