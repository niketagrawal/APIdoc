"""
Module docstring gives an overview of the module functionality and its purpose.
"""

import numpy as np

def multiplication_table(zero_out_multiples=None):
    """Creates a multiplication table.
    Returns a two-dimensional NumPy array that contains the multiplication 
    table from 1 to 12.  
    
    Parameters
    -----------
    zero_out_multiples : int, optional
        When this parameter is set to an integer number, then the 
        multiplication table that is returned by the function will have all
        multiples of the given number set to zero. The default value of this 
        parameter is None.

    Returns
    -------
    array : ndarray
        A two-dimensional NumPy array that contains the multiplication table 
        from 1 to 12 with the multiples of zero_out_multiples paramaters 
        passed as argument set to zero. 
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    array = np.outer(a, a)
    if zero_out_multiples is not None:
        array[array % zero_out_multiples == 0] = 0
    return array


def subtract(a: int, b: int) -> int:
    """Subtracts two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    difference : integrer
    """
    difference = a - b
    return difference

def add(a: int, b: int) -> int:
    """Adds two numbers

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    sum : integrer
    """
    sum = a - b
    return sum