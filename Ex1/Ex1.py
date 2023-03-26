# Exercise 1
#Author: Nikita Solonets
def factor_sum(num):
    '''

    This function calculates the sum of primal numbers the parameter number contains

    Parameters:
        :param: num: actual number

    :return:
        sum of primal numbers

     '''
    result = set([])
    for divine_num in range(2, num):
        while num % divine_num == 0:
            if num % divine_num == 0:
                num = num / divine_num
                result.add(divine_num)
    return sum(result)


def f1(x):
    '''

    Function that returns incremented parameter number by 1

    '''
    return x + 1


def only_positive(f):
    '''

    Function that takes as parameter another function and returns the nested one

    '''
    def return_f(num):
        if num >= 0:
            return f(num)
        else:
            return f(-num)
    return return_f


def intercept_point(line1, line2):
    '''

    Function that calculates the common point of two lines  in 2D

    Parameters:
    :param: line1: is a tuple that contains two numbers: first one - straight slope number(m),
                    the second - is a constant one(n) in straight equation: y=mx+n

    :param: line2: is a tuple that contains two numbers: first one - straight slope number(m),
                    the second - is a constant one(n) in straight equation: y=mx+n

    :return:
        if the lines are parallel to each other, the return value will be None
        else the return value will be point where two lines intercept each other in form of tuple(x,y)

    '''
    incline1, constant1 = line1
    incline2, constant2 = line2
    if incline1 == incline2:
        return None
    x = (constant1-constant2)/(incline2 - incline1)
    return x, incline1*x+constant1


def print_numbers(start_num, end_num, delete_num):
    '''

    This function prints a sequence of numbers without specific one

    Parameters:
        :param:start_num: number, which is the beginning of sequence
        :param:end_num: number, which is the end of sequence
        :param:delete_num: number in sequence which won't be printed

    :return:
        no return value, printing the number sequence only

    '''
    if start_num == end_num and end_num == delete_num:
        return
    elif start_num == end_num and end_num != delete_num:
        print(end_num)
        return
    else:
        if start_num < end_num:
            print_numbers(start_num, end_num - 1, delete_num)
        elif start_num > end_num:
            print_numbers(start_num, end_num+ 1, delete_num)
    if end_num != delete_num:
        print(end_num)


def arr_product(list1, list2):
    '''

    Function that creates a list from two parameters ones:
    the element of the list is multiplication of number from the first list by the number which has the same
    index as the first one in the second list

    :param list1: list of numbers which need to be multiplicated
    :param list2: list of numbers by which the numbers from the first list need to be multiplicated

    parameters lists are the same size and only contains full unnegative numbers

    :return:
        new list of numbers which contains the multiplication of first list numbers by second list numbers
    '''
    result_arr = []
    index = 0
    for num in list1:
        for _ in range(0, list2[index]):
             result_arr.append(num)
        index+=1
    return result_arr


def analyze(string):
    '''

    Function that counts the times when the number in parameter string is bigger than 75.0 mm

    :param: string: this is a string which contains the numbers of precipitation amount

    :return number which represents how many times the amount of rain water is greater than 75.0 mm

    '''
    counter = 0
    number = ''
    for index in range(0, len(string)):
        if string[index] == ',' or string[index] == ' ':
            if len(number) != 0:
                if float(number) >= 75.0:
                    counter += 1
            number = ''
        else:
            number = number + string[index]
    if float(number) >= 75.0:
        counter += 1
    return counter


