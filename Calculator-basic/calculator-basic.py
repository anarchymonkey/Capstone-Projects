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
    divide = 0
    """
    empty list to store all the variables 
    
    """

    list1 = []

    """
    will take input untill the user types 0 
    
    """
    while True:

        n = int(input("please enter the  numbers"))

        list1.append(n)


        if n==0:
            break




    if choice == '1':
       for i in range(0,len(list1)+1):
           sum += list1[i]

       print(sum)

    elif choice == '2':
        for i in range(0,len(list1)):

            diffrence = list1[i] - diffrence


        print(diffrence)






