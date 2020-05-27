import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        print("Hello")
        n = int(input())

        ar = list(map(int, input().rstrip().split()))

        result = sockMerchant(n, ar)

        fptr.write(str(result) + '\n')

        fptr.close()


sockMerchant(3, 3)
