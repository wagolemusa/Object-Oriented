import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the sockMerchant function below.
# x = [10, 20, 20, 10, 10, 30, 50, 10, 20]
def sockMerchant(n, ar):
    n = int(raw_input())
    c = map(int, raw_input().split()),
    ans = 0
    for val in [len(list(group)) for key, group in groupby(sorted(c))]:
        ans = ans + val/2
    return ans

print(sockMerchant(ans))

