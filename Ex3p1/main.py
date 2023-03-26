# Exercise 4 part 1
#Author: Nikita Solonets
#ID: 340961408
class Shekel():
    '''
    THis class represents a shekel currency
    '''
    def __init__(self, num):
        '''
        constructor to hold a sum in shekels
        :param num:
        '''
        self.__sum = num

    def __repr__(self):
        '''
        string representation of object for python
        :return: a string with expression of object creation to execute
        '''
        return f'Shekel({self.__sum})'

    def __str__(self):
        '''
        string representation of shekels to print
        :return: understandable string representation of shekel
        '''
        return f'{self.__sum}nis'

    @property
    def dollar(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of shekels in dollars
        '''
        return self.amount()*rates[('dollar', 'nis')]

    @property
    def shekel(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of shekels in shekels
        '''
        return self.__sum

    @property
    def euro(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of shekels in euros
        '''
        return self.amount()*rates[('euro', 'nis')]

    def amount(self):
        '''
        Method to return a sum in shekels
        :return: sum in shekels
        '''
        return self.__sum


class Dollar():
    '''
    THis class represents a shekel currency
    '''
    def __init__(self, num):
        '''
        constructor to hold a sum in dollars
        :param num:
        '''
        self.__sum = num

    def __repr__(self):
        '''
        string representation of object for python
        :return: a string with expression of object creation to execute
        '''
        return f'Dollar({self.__sum})'

    def __str__(self):
        '''
        string representation of dollars to print
        :return: understandable string representation of shekel
        '''
        return f'{self.__sum}$'

    @property
    def shekel(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of dollars in shekels
        '''
        return rates[('dollar', 'nis')] * self.__sum

    @property
    def dollar(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of dollars in dollars
        '''
        return self.__sum

    @property
    def euro(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of dollars in euros
        '''
        return self.amount()/rates[('euro', 'nis')]

    def amount(self):
        '''
        Method to return a sum in shekels
        :return: sum in shekels
        '''
        return self.shekel


class Euro():
    '''
    THis class represents a shekel currency
    '''
    def __init__(self, num):
        '''
        constructor to hold a sum in euros
        :param num:
        '''
        self.__sum = num

    def __repr__(self):
        '''
        string representation of object for python
        :return: a string with expression of object creation to execute
        '''
        return f'Euro({self.__sum})'

    def __str__(self):
        '''
        string representation of euros to print
        :return: understandable string representation of shekel
        '''
        return f'{self.__sum}€'

    @property
    def shekel(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of euros in shekels
        '''
        return rates[('euro', 'nis')] * self.__sum

    @property
    def dollar(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of euros in dollars
        '''
        return self.shekel/rates[('dollar', 'nis')]

    @property
    def euro(self):
        '''
        This method serves for conventional interface purposes to return this number in shekels
        :return: sum of euros in euros
        '''
        return self.__sum

    def amount(self):
        '''
        Method to return a sum in shekels
        :return: sum in shekels
        '''
        return self.shekel


def add(curr1, curr2):
    '''
    FUcntion to return a sum of different currencies in shekels
    :param curr1: first currency
    :param curr2: second currency
    :return: sum in shekels
    '''
    return curr1.shekel + curr2.shekel


def apply(action, curr1, curr2):
    '''
    Function to apply a specific action on two currencies
    :param action: action to execute
    :param curr1: first currency
    :param curr2: second currency
    :return: an object with first currency type and sum in this currency
    '''
    action_dict = {('add', 'nis'): lambda x,y: x.shekel + y.shekel,
                   ('add', 'dollar'): lambda x,y: x.dollar + y.dollar,
                   ('add', 'euro'): lambda x,y: x.euro + y.euro,
                   ('sub', 'nis'): lambda x,y: x.shekel - y.shekel,
                   ('sub', 'dollar'): lambda x,y: x.dollar - y.dollar,
                   ('sub', 'euro'): lambda x,y: x.euro - y.euro
                   }
    current_sum = action_dict[(action,help_dict[type(curr1)])](curr1, curr2)
    return eval(repr(f'{type(curr1).__name__}({round(current_sum, 2)})'))


Shekel.__add__ = lambda self, other: self.shekel + other.shekel
Dollar.__add__ = lambda self, other: self.dollar + other.dollar
Euro.__add__ = lambda self, other: self.euro + other.euro

rates = {('dollar', 'nis'): 3.82, ('euro', 'nis'): 4.07}
help_dict = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}
coercions = {'dollar': lambda x: Shekel(round(x.amount(),2)),
             'euro': lambda x: Shekel(round(x.amount(),2)),
             'nis': lambda x: Shekel(round(x.amount(),2)),
             ('dollar', 'nis'): lambda x: Shekel(round(x.amount(),2)),
             ('euro', 'nis'): lambda x: Shekel(round(x.amount(),2)),
             ('nis', 'nis'): lambda x: x
             }


def coerce_apply(action, curr1, curr2):
    '''
    This function returns a sum i shekels from two different currencies
    :param action: action to execute
    :param curr1: first currency
    :param curr2: second currency
    :return: an object with shekel type and sum in shekels
    '''
    action_dict = {'add': lambda x,y: x.amount() + y.amount(), 'sub': lambda x,y: x.amount()-y.amount()}
    if type(curr1) != Shekel:
        curr1 = coercions[help_dict[type(curr1)]](curr1)
    if type(curr2) != Shekel:
        curr2 = coercions[help_dict[type(curr2)]](curr2)
    current_sum = action_dict[action](curr1, curr2)
    return repr(f'Shekel({round(current_sum, 2)})')
