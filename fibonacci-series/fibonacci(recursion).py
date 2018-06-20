"""
docstring: fibonacci series by recursion

"""


def fibo_recur(num):
    if num == 0:

        return 0

    elif num == 1:

        return 1
    else:

        return (fibo_recur(num - 1) + fibo_recur(num - 2))


if __name__ == "__main__":

    n = int(input('Please Enter The Terms to which the sequence will go'))

    for i in range(0, n):
        print(fibo_recur(i))
