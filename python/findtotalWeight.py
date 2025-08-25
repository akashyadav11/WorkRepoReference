#!/bin/python3

import math
import os
import random
import re
import sys


def findTotalWeight(products):
    # Debugging area starts here.
    ans = 0
    while(len(products)):
        idx = 0
        for i in range(len(products)):
            if products[i] < products[idx]:
                idx = i
        ans += products[idx]
        temp_arr = []
        for i in range(len(products)):
            if i == idx - 1 or i == idx + 1 or i==idx:
                continue
            temp_arr.append(products[i])
        products = temp_arr
    return ans
    #Debugging area ends here.
products=[4,3,2,1]
result = findTotalWeight(products)
print(result)



