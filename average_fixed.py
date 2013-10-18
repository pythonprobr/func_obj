"""

>>> avg = make_cumulative_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value',)
>>> avg.__code__.co_freevars
('num_items', 'total')
>>> avg.__closure__  # doctest: +ELLIPSIS
(<cell at 0x...: int object at 0x...>, <cell at 0x...: int object at 0x...>)
>>> avg.__closure__[0].cell_contents
3
>>> avg.__closure__[1].cell_contents
33
"""

def make_cumulative_averager():
    num_items = 0
    total = 0
    def averager(new_value):
        nonlocal num_items, total
        num_items += 1
        total += new_value
        return total / num_items
    return averager
