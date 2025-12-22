import numpy as np
# to generate a vector
vector1 = np.array([1.0, 2.0, 3.0])     # Dim 1
vector2 = np.array([4.0, 5.0, 6.0])

#inner product would be basically 
# 1.0 * 4.0 + 2.0 *5.0 + 3.0 * 6.0 
# = 4 + 10 + 18 
# = 32
np.inner(vector1, vector2)
vector1 @ vector2

# if we wanna do elementwise product we'll do:
vector1 * vector2
np.multiply(vector1, vector2)

# for addition and subtraction we can simply do + and -

#To find out which names a module has defined use dir(module_name)

#To see what is in a folder:    !tree folder_name

#Getting help: help() or ?function

#unittest: Built-in unit testing framework
#pytest: simple, scalable       -> remember to import pytest
#doctest: test documentation

#'assert  blabla == blablab' to check the conditions in tests

# @pytest.mark.parametrize #multiple sets of inputs
# @pytest.fixture

# %timeit% function(100)


#Stats instance by supplying a file name to the constructor:
import pstats
stats = pstats.Stats(module.function)
stats.strip_dir() # is used when working with profiling results from modules like cProfile or profile.
stats.strip_dir().sort_stats('column')  # Clean up file paths, sort by the column
stats.strip_dir().sort_stats('column').print_stats(10) # print top 10
