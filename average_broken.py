"""

>>> avg = make_cumulative_averager()
>>> avg(10)
Traceback (most recent call last):
  ...
UnboundLocalError: local variable 'total' referenced before assignment

"""

def make_cumulative_averager():
    num_items = 0
    total = 0
    def averager(new_value):
        new_average = (new_value + total * num_items) / (num_items + 1)
        total += new_value
        num_items += 1
        return new_average
    return averager
