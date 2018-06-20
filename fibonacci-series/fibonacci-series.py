"""
docstring: Programme to implement fibonacci series

"""

if __name__ == "__main__":

    '''
    number1,number2,next_Term:var
    fibonacci sequence of diffrent numbers:output
    
    '''

    number1 = 0
    number2 = 1

    last_term = int(input("Enter the term to which the series should continue :: "))
    print(number1)
    print(number2)
    for i in range(0, last_term):
        next_number = number1 + number2
        number1 = number2
        number2 = next_number
        print(next_number)