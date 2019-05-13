#!/usr/bin/env python
# In case of poor (Sh***y) commenting contact adam.lamson@colorado.edu
# Basic
import sys
import os
import molssi_devops as md
import pytest
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


def test_title_case():
    """! Test title case function
    @return: TODO

    """
    test_str = "THIS IS A STRING"
    title = md.util.title_case(test_str)
    assert title == "This Is A String "


@pytest.mark.my_test
def test_title_case_error():
    """! Test title case function
    @return: TODO

    """
    test_str = ['THIS', 'IS', 'A', 'STRING']
    with pytest.raises(TypeError):
        title = md.util.title_case(test_str)


##########################################
if __name__ == "__main__":
    print("Not implemented yet")
