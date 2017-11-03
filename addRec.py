def increment(number):
    '''
    objective: To increment a number by 1
    input values:
        number: The number to be incremented

    output value: The Incremented number
    '''
    #approach: Add the number with 1
    
    return number+1

def add(num1,num2):
    '''
    objective: To add two numbers without loop or conditional statements
    input values:
         num1: the first number
         num2: the second number
    output:
         The incremented number
    '''
    #approach: use the increment function

    assert num1 >= 0
    assert num2 >= 0

    if num2 == 0:
        return num1
    return add(increment(num1),num2-1)


num1 = int(input('Enter the first Number: '))
num2 = int(input('Enter the second number: '))

print('The sum is = ',add(num1,num2))
