import doctest
def palindrome_check(string):
    '''
    >>> palindrome_check('лепсспел')
    True
    >>> palindrome_check('HelloWorld!')
    False
    '''
    if string == string[::-1]:
        return True
    return False

doctest.testmod(verbose=True) #Для проверки - Всё работает!!!


