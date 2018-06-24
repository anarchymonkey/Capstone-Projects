"""

Programme to check weither a string , integer  is a palindrome or not

"""


def pal(string):
    STRING_NEW = string.replace(" ","")
    LENGTH = len(STRING_NEW)

    for i in range(0, LENGTH-1):

        if STRING_NEW[i] == STRING_NEW[LENGTH-1-i]:
            return True
        else:
            return False


if __name__ == "__main__":
    str1=input('Enter a string')
    pal(str1)
    print(pal(str1))


"""
Works for test cases with spaces also s
"""