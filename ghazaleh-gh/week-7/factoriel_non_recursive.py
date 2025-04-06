"""
تمرین اول: تابع فاکتوریل را بدون استفاده از recursion و به کمک current  و previous بنویسید.
"""
def non_rec_fact(num):
    previous, current = num, num-1
    if num == 0:
        return 1

    while current > 0:
        previous, current = previous * current, current-1
    return previous


def rec_fact(num):
    if not num:
        return 1
    result = num * rec_fact(num - 1)
    return result


print("non-recursive factorial -> ", non_rec_fact(5))
print("recursive factorial -> ", non_rec_fact(5))
