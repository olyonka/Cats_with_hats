import numpy as np
import math

# a. Create an array with shape (4, 3)
# a. all zeros
zeros_array = np.zeros((4, 3))
print("Zeros array:\n", zeros_array)

# b. ones
ones_array = np.ones((4, 3))
print("Ones array:\n", ones_array)

# c. numbers from 0 to 11
numbers_array = np.arange(12).reshape(4, 3)
print("Numbers array:\n", numbers_array)

# b. Tabulate the function F(x) = 2x^2 + 5, x ∈ [1, 100] with step 1
x_values = np.arange(1, 101, 1)
f_x = 2 * x_values ** 2 + 5
table_b = np.column_stack((x_values, f_x))
print("Table for F(x) = 2x^2 + 5:\n", table_b)

# c. Tabulate the function F(x) = e^(-x), x ∈ [-10, 10] with step 1
x_values = np.arange(-10, 11, 1)
f_x = np.exp(-x_values)
table_c = np.column_stack((x_values, f_x))
print("Table for F(x) = e^(-x):\n", table_c)