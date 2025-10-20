def isSubset(num1, num2):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(len(num2) - len(num1) + 1):
        if num1 == num2[i:i+len(num1)]:
            return True
    return False


def main():
    num1 = [20, 30, 35]
    num2 = [5, 20, 30, 35, 50]
    print(f'\n****************** Test Case 1 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}, expected True')  # True

    num1 = [1, 3, 2]
    num2 = [1, 2, 3, 4, 5]
    print(f'\n****************** Test Case 2 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}, expected False')  # False

    num1 = [1, 4, 5]
    num2 = [1, 2, 3, 4, 5]
    print(f'\n****************** Test Case 3 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}, expected False')  # False

    num1 = [1, 3, 2]
    num2 = [4, 1, 3, 2, 5]
    print(f'\n****************** Test Case 4 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}, expected True')  # True


if __name__ == '__main__':
    main()
