"""
تمرین دوم:‌rangeای بنویسید که اعداد اعشاری generate کند مثلا range(2.3, 3.78, 0.01) یعنی از 2.3 شروع کند تا 3.78 با استپ 0.01
"""

def float_range(start, end , step):
    while start < end:  # [start, end)
        yield start
        start += step


for i in float_range(2.30, 3.78, 0.01):
    print(i)
