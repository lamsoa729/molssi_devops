#!/usr/bin/env python
# In case of poor (Sh***y) commenting contact adam.lamson@colorado.edu
# Basic
import sys
import os
import molssi_devops as md
import pytest
import numpy as np
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


@pytest.mark.parametrize("num_list, expected_mean", [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000 / 2.0)
])
def test_math_sum_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(md.mean(num_list), expected_mean, 1e-6)


def test_molssi_math_mean():
    """!Test the mean function in molssi devops
    @return: TODO

    """
    assert md.mean([1, 2, 3, 4, 5]) == 3
    assert md.mean([0, 0, 0]) == 0


@pytest.mark.my_test
def test_molssi_math_mean_2():
    """!Test the mean function in molssi devops
    @return: TODO

    """
    assert md.mean([-1.5, 0]) == -.75


##########################################
if __name__ == "__main__":
    print("Not implemented yet")
