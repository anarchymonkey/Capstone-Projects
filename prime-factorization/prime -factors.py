"""

dfact=: a programme for prime factorization by using python

"""

def prime_fact(num):

    i = 1
    while  i <=num:

        k=0
        #  checking weither they are factors or not
        if(num%i==0):

            j=1

            while j<=i:
                # checking weither prime factors or not
                if i%j == 0:
                    k = k+1
                j = j+1
            if k==2:
                print(i)
        i=i+1


if  __name__ == "__main__":
    """
    n = number :var
    number :output
    
    """

    n = int(input("Please Enter a number : ---> "))
    prime_fact(n)





