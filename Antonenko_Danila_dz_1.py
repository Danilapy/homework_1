# 1 задание  Convert seconds to days, hours and minutes

# duration = int(input())
# d, h, m, s = duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60
# print(f'{d} дней {h} часов {m} мин {s} cек')


# 2 задание
# nmbcube = [i ** 3 for i in range(1, 1001, 2)]
#
# tot = 0
# for n in nmbcube:
#     while n > 0:
#         dig = n % 10
#         tot = tot + dig
#         n = n // 10
#     # print(tot)
#     if tot % 7 == 0:
#         print(tot)
# # понял как получить суммы цифр чисел которые делятся на 7 без остатка,а как теперь получить эти числа не понял :D
#

# 3 задание
# for s in range(1, 101):
#
#     if s % 10 == 1 and s % 100 != 11:
#         print(s, 'процент')
#     elif 2 <= s % 10 <= 4 and (s % 100 < 10 or s % 100 > 20):
#         print(s, 'процента ')
#     else:
#         print(s, 'процентов')
