"""
تمرین سوم: rangeای بنویسید که روی حروف الفبا جلو برود یعنی مثلا range(c,x,2) از c شروع تا x برود با استپ 2
"""

# def alphabetic_range(start_char = 'a', end_char = 'z', step = 1):
#     alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
#
#     start = alphabet_string.index(start_char.lower())
#     end = alphabet_string.index(end_char.lower())
#     while start < end:
#         yield alphabet_string[start]
#         start += step


def alphabetic_range(start_char='a', end_char='z', step=1):
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'

    start = alphabet_string.index(start_char.lower())
    end = alphabet_string.index(end_char.lower())

    if step > 0:
        while start < end:
            yield alphabet_string[start]
            start += step
    else:
        while start > end:
            yield alphabet_string[start]
            start += step


if __name__ == "__main__":
    for i in alphabetic_range('z', 'a', -2):
        print(i)
