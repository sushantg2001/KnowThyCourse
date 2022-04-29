from bm25 import bm25output
from filter import filter
import os
print(os.getcwd())
filters = [
    float(4.0),
    [True, True, True, True],
    [True, True, True]
]
result = bm25output("database mongo", 20)
filtered_result = filter(result, filters)
print(filtered_result)