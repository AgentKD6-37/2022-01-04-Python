#!/usr/bin/python3

def calc_upper_lower(string_phrase: str):
    """function takes in a phrase and calculates the upper and lowercase characters within it excluding spaces and
    '.' """
    upper_sum = 0
    lower_sum = 0
    for char in string_phrase:
        if char != " ":
            if char != ".":
                if char.isupper():
                    upper_sum += 1
                else:
                    lower_sum += 1
    print(f"Upper case characters: {upper_sum}\nLower case characters: {lower_sum}")


def sum_of_all(list_of_nums: list):
    """adds all numbers in a list together and returns the sum"""
    sum_of_nums = 0
    for num in list_of_nums:
        sum_of_nums += num
    print(sum_of_nums)
    return sum_of_nums


def print_even(list_of_nums: list):
    """prints only the even numbers in a given list of numbers"""
    for num in list_of_nums:
        if num % 2 == 0:
            print(num)


def multiply_all(list_of_nums: list):
    """"multiplies all numbers together in a given list of numbers"""
    result_of_mult = 1
    for num in list_of_nums:
        result_of_mult *= num
    print(result_of_mult)
    return(result_of_mult)


calc_upper_lower("Cells Interlinked Within Cells")
test_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_all(test_of_nums)
print_even(test_of_nums)
multiply_all(test_of_nums)