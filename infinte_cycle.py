import itertools as seq

def forever_cycle(iterable):
    '''
    Python program to generate an infinite cycle of elements from an iterable.
    PS:The iterable data type should be a list or a string or a dictionary, etc
    '''
    return seq.cycle(iterable)
# Following  loops will run forever    
result = forever_cycle(['me','you','them','us'])
print("The said function print never-ending items:")
for i in result:
    print(i)
