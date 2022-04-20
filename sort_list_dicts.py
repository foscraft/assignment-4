
def sort_listdict(listdict):
    """
    Python program to sort a list of dictionaries using Lambda.
    """
    return sorted(listdict, key=lambda i: i['name'])


ages = [{'name': 'meek', 'age': 40}, {'name': 'andrew', 'age': 20}, {'name': 'albert', 'age': 30}]
#invoking the function
print(sort_listdict(ages))