'''Условие задачи "Хаотичность погоды":
Метеорологическая служба вашего города решила исследовать погоду новым способом.

Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше,
чем в день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.
'''

'''Формат ввода:
В первом элементе кортежа дано число n — длина периода измерений в днях.
Во втором элементе кортежа даны n целых чисел — значения температуры в каждый из n дней.
'''

'''Формат вывода:
Выведите единственное число — хаотичность за данный период.
'''

# Пример ввода -> вывода:
inputs = [
    ('7', '-1 -10 -8 0 2 0 5'),  # -> 3
    ('5', '1 2 5 4 8'),          # -> 2
    ('1', '4')                   # -> 1
]

# тут ваше решение:
def cnt_day(*args):
    count = 0
    last_idx = len(args) - 1

    for i, value in enumerate(args):
        if i == 0:
            continue
        if i != last_idx:
            if args[i - 1] < value > args[i + 1]:
                count += 1
        else:
            if args[i - 1] < value:
                count += 1

    return count


print(cnt_day(1, 2, 3, 5, 4, 8))   # 2