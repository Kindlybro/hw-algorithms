'''Условие задачи "Cкобочная последовательность":
Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

- пустая строка - правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного типа, – правильная скобочная последовательность;
- правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью — тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.
'''

'''Формат ввода:
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.
'''

'''Формат вывода:
Выведите «True» или «False».
'''

# Пример ввода -> вывода:
inputs = [
    '[{()}]',    # -> True
    '()',   # -> True
    '()[])',  # -> False
    '',  # -> True
    '[]{)'  # -> False
]


# Используйте написанный класс Stack:
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]


if __name__ == '__main__':
    inp_line = list(input())
    stack = Stack()
    for value in inp_line:
        if value in PATTERN.keys():
            stack.push(value)
        elif not stack.isEmpty() and PATTERN.get(stack.peek()) == value:
            stack.pop()
        else:
            stack.push(value)
    if stack.isEmpty():
        print('True')
    else:
        print('False')