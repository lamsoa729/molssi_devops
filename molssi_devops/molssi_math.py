"""
molssi_math.py
A package of useful math functions

Handles the primary functions
"""


def mean(my_list):
    """!Calculate the mean of the list.

    @param my_list: list of python objects that can be summed (float, int, etc.)
    @return: Mean of my_list (float)

    """
    return sum(my_list) / len(my_list)


def canvas(with_attribution=True):
    """!Math of the molssi

    @param with_attribution: bool, Optional, (default=True)
        Set whether or not to display who the quote is from
    @return: quote (str)
        Compiled string including quote and optional attribution

    """
    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


# def canvas(with_attribution=True):
#     """
#     Placeholder function to show example docstring (NumPy format)

#     Replace this function and doc string for your own project

#     Parameters
#     ----------
#     with_attribution : bool, Optional, default: True
#         Set whether or not to display who the quote is from

#     Returns
#     -------
#     quote : str
#         Compiled string including quote and optional attribution
#     """


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
