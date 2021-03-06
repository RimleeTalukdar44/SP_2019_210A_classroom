#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


def walnut_party(walnuts, is_weekend):
    if walnuts > 39 and is_weekend is True:
        return True
    elif walnuts > 39 and walnuts < 61:
        return True
    else:
        return False
    pass
