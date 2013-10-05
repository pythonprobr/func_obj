#!/usr/bin/env python

# Simple closure example in Python adapted from
# http://www.perlmonks.org/?node_id=630664

# Use a closure here, so we don't have to load this private
# data more than once.
def monthConverterFactory():
    months = dict(
        Jan = 0,
        Feb = 1,
        Mar = 2,
        Apr = 3,
        May = 4,
        Jun = 5,
        Jul = 6,
        Aug = 7,
        Sep = 8,
        Oct = 9,
        Nov = 10,
        Dec = 11 
    )
    return lambda name: months[name]
        
monthConverter = monthConverterFactory();

print monthConverter('Mar')

