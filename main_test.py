import main
import pytest

@pytest.mark.basic
def test_main_1():
    num1 = [20, 30, 35]
    num2 = [5, 20, 30, 35, 50]
    print(f'\n****************** Test Case 1 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}, expected True')  # True
    assert ret == True, f'Expected True but got {ret}'

@pytest.mark.edge
def test_main_2():
    num1 = [1, 3, 2]
    num2 = [1, 2, 3, 4, 5]
    print(f'\n****************** Test Case 2 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}, expected False')  # False
    assert ret == False, f'Expected False but got {ret}'    

@pytest.mark.edge
def test_main_3():
    num1 = [1, 4, 5]
    num2 = [1, 2, 3, 4, 5]
    print(f'\n****************** Test Case 3 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}, expected False')  # False
    assert ret == False, f'Expected False but got {ret}'

@pytest.mark.bonus
def test_main_4():
    num1 = [1, 3, 2]
    num2 = [4, 1, 3, 2, 5]
    print(f'\n****************** Test Case 4 ******************')
    print(f'num1: {num1}, num2: {num2}')
    ret = main.isSubset(num1, num2)
    print(f'Your return value is {ret}, expected True')  # True
    assert ret == True, f'Expected True but got {ret}'
