# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два
# соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве
# внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких
# собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального
# числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
bush_amount = int(input('type amount of bushs: ')) # кол-во кустов
berries_list = [int(input('type amount of berries: ')) for i in range(bush_amount)] # кол-во ягод на 1 кусте на грядке
res_list = []
res1 = berries_list[0] + berries_list[-1] + berries_list[-2]
res_list.append(res1)
res2 = berries_list[0] + berries_list[1] + berries_list[-1]
res_list.append(res2)
for berries in range(2, len(berries_list)):
    res = berries_list[berries] + berries_list[berries - 1] + berries_list[berries - 2]
    res_list.append(res)
print(max(res_list))


