"""
寻找水仙花数。

说明：水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。

Version: 0.1
Author: usrpi
Date: 2020-08-06
"""

for num in range(100, 1000):
    low = num % 10 #个位数，取模
    mid = num // 10 % 10 #十位数，先整除，再取模
    high = num // 100 #百位数，整除
    if low ** 3 + mid ** 3 + high ** 3 == num:
        print(num)    