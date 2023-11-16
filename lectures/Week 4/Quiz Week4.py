# def process_string(s):
#     # Split the string into a list of words and convert them to lowercase
#     words = s.split()
#     words = [word.lower() for word in words if word.isalnum()]
#     return words
# print(process_string("This is my test String"))

# def process_string(s):
#     words = s.split()
#     result = []
#
#     for i, word in enumerate(words):
#         if i % 2 != 0:
#             result.append(word.upper())
#         else:
#             result.append(word.lower())
#
#     return result
# print(process_string("This is my test String"))

# def my_function(x):
#     x = x + 1
#     return x
#
# x = 3
# my_function(x)
# print (x)
# def my_function(y):
#     # global y
#     y = y + x
#     x = 2
#     y = y + x
#     return y
#
# x = 3
# y = 10
# y = my_function(x)
# print(y)
# def get_five():
#     return 5
#
# def get_and_print_five():
#     five = get_five()
#     print(f'Called get_five(): result is {five}')
#
# get_and_print_five()
prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# 2. Replace the prc_dic key for '3000-01-15' with '2020-01-15'
prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15')


# 1. Define a variable sorted_keys containing the keys of prc_dic in ascending order
sorted_keys = [key for key in sorted(prc_dic.keys())]
print(sorted_keys)
