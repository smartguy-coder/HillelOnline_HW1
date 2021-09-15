"""
work module for writing in file the sum of numbers (from 1 to 100),
that can be divided on given number from the file 'denom.txt'
"""

import os


def current_directory() -> None:
    """to be sure that current working directory is located where *.py file is located"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())  # for debug purposes


def get_denominator() -> int:
    """
    Read from the file denom.txt (located in current directory) one number.
    File must exist and contain just one number.

    This function manages 3 exceptions:
     - the file 'denom.txt' does not exist
     - the file  'denom.txt' contains not a number
     - the number is 0 (zero)

    :return: int
    """
    # just in case we change current working directory before opening the file denom.xtx
    current_directory()

    try:
        with open('denom.txt', mode='r', encoding='UTF-8') as f:
            denominator = int(f.read())
    except FileNotFoundError:
        print('\033[1;31mFile "denom.txt" does not exist in the current directory.\033[0m')
        return None
    except ValueError:
        print('\033[1;31mFile "denom.txt" contains not a number.\033[0m')
        return None

    if denominator:
        return denominator
    else:
        print('\033[1;31mFile "denom.txt" contains 0 (zero).\033[0m')


def get_list_of_numbers(denominator: int) -> list:
    f"""
    return the list with the integer numbers, that can divide on given number: {denominator},
    numbers in range (0:100]

    :param denominator:
    :return: list
    """
    list_of_numbers = [number for number in range(1, 101) if (number % denominator == 0)]

    return list_of_numbers


def get_sum(list_of_numbers: list) -> int:
    """
    count the total sum of all numbers in a given list

    :param list_of_numbers:
    :return: int
    """
    total_sum = sum(list_of_numbers)

    return total_sum


def write_result_in_file(number: int) -> None:
    """
    function writes the given number in the file 'result.txt'

    :param number:
    :return: None
    """

    with open("result.txt", mode='w', encoding='UTF-8') as file:
        file.write(str(number))

    return None


if __name__ == '__main__':
    print('\033[43mYou are running the support module for main.py file.\033[0m')
