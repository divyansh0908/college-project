d = {'a': 3, 'b': 2, 'c': 3, 'd': 4}
 
from itertools import islice
 
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
 
n_items = take(2, d.items())
 
print (n_items )