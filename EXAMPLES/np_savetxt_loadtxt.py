#!/usr/bin/env python
import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=np.uint8,
)

print(sample_data)
print('-' * 60)

float_file_name = 'save_data_float.txt'

np.savetxt(float_file_name, sample_data, delimiter=",", fmt="%.2f")  # <3>

int_file_name = 'save_data_int.txt'

np.savetxt(int_file_name, sample_data, delimiter=",", fmt="%d")  # <4>

data = np.loadtxt(float_file_name, delimiter=",")  # <5>
print(data)
