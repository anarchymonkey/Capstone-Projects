"""
docstring :: Trial to build a working calculator

basic functionalities :output

"""



if __name__ == "__main__":
    choice = str(input("What do you wanna do :---> \n press 1 for add \n press 2 for substract \n press 3 for divide "
                       "\n press 4 for multiplicaton \n press 5 for modulus :: \n "))


    """
    
    variable assignment initialize : 
    
    
    
    """
    sum = 0
    diffrence = 0
    product = 1
    divide = 1
    mod = 1
    """
    empty list to store all the variables 
    
    """

    list1 = []


    """
    will take input untill the user types 0 
    
    """
    while True:

        n = int(input("please enter the  numbers :----> "))

        list1.append(n)

        str1 = str(input('\t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t \t do you want to get the ans? press y or n'))
        if str1 =='Y'.lower():
            break




    if choice == '1':
       for i in range(0,len(list1)+1):
           sum += list1[i]

       print(sum)

    elif choice == '2':
        for i in range(0,len(list1)):

            diffrence =list1[i]-diffrence


        print(diffrence)

    elif choice == '3':
        for i in range(0, len(list1)):

            product = list1[i] * product

        print(product)

    elif choice == '4':

        for i in range (0,len(list1)):
            divide = list1[i]/divide
        print(divide)

    elif choice == '5':

        for i in range(0, len(list1)):

            mod %= list1[i]

        print(float(mod))









