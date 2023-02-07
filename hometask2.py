# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = 99# int(input('type number: '))
multiplier = 2
multi_list = []
while multiplier != number:
    if number % multiplier == 0:
        multi_list.append(multiplier)
        number = number//multiplier
    else:
        multiplier +=1
multi_list.append(number)
print(multi_list)
