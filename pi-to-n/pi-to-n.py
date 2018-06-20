"""

Docstring: pi To n numbers

"""



pi = lambda  : 22/7







if __name__ == "__main__":


    n = int(input("Tell me to how many terms you wanna keep pi to"))

    print("%.{}f".format(n)%pi())