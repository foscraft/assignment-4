def max_min(lst):
    '''
    Python program to find the maximum and minimum values in a given list
    of tuples using a lambda function
    '''
    # list of tuples
    
    # using a lambda function to find the maximum and minimum values
    print(f"The maximum value is {max(lst, key=lambda x: x[0])}")
    print(f"The minimum value is {min(lst, key=lambda x: x[0])}")

lk = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#invoking the function
max_min(lk)