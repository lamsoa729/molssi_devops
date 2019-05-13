#!/usr/bin/env python
# In case of poor (Sh***y) commenting contact adam.lamson@colorado.edu
# Basic
import sys
import os
# Testing
# import pdb
# import time, timeit
# import line_profiler
# Analysis
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import h5py
# import yaml
# from math import *
# Speed
# from numba import jit
# Other importing
# sys.path.append(os.path.join(os.path.dirname(__file__), '[PATH]'))


"""@package docstring
File:
Author: Adam Lamson
Email: adam.lamson@colorado.edu
Description:
"""


def title_case(title_string):
    """!Change string so first letter of every word is upper case and the other letters are lowercase.

    @param title_string: TODO
    @return: TODO

    """
    words = title_string.split()
    title = ""
    for word in words:
        title += word[0].upper() + word[1:].lower() + " "

    return title


##########################################
if __name__ == "__main__":
    print("Not implemented yet")
