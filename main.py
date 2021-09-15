"""
Kartychak V. HW1
Python advance course from Hillel (started 22.07.2021), online
16.09.2021
"""

import os
import work_module


def current_directory() -> None:
    """to be sure that current working directory is located where this *.py file is located"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())  # for debug purposes


def main_engine() -> None:
    """
    main function to execute the homework
    :return: None
    """

    # just in case we change current working directory before opening the file denom.xtx
    current_directory()

    try:
        denominator = int(work_module.get_denominator())
    except TypeError:
        print('\033[1;31mThe program cannot write sum of the numbers in a file.\033[0m')
        return None

    list_of_numbers = work_module.get_list_of_numbers(denominator)
    total_sum = work_module.get_sum(list_of_numbers)
    work_module.write_result_in_file(total_sum)
    print(f'total sum = {total_sum}')
    print("The file was written successfully.")


if __name__ == '__main__':
    main_engine()


