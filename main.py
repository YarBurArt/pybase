from datetime import datetime
import time
import math
import numpy
# импорт библиотек


def logging(func):  # декоратор для логирования, принимает в аргумент саму функцию
    time_log_dt = datetime.now()  # вызов функции настоящего времени сейчас в формате гггг-мм-дд чч:мм:сс.мс
    time_log_str = str(time_log_dt)  # преобразование неявного типа
    print("[SYSTEM_LOG] function start in " + time_log_str)  # конкатенация строк

    def wrapped():  # наследование аргументов декорируемой функции
        start_time = time.perf_counter()  # perf counter - время начала выполнения
        res = func()  # само выполнение с наследованием аргументов
        print(time.perf_counter() - start_time)  # разница, длительность выполнения функции
        return res  # поднять результат в функцию выше

    try:  # попытаться просмотреть время работы вызвав декорируемую функцию
        print( "[SYSTEM_LOG] function run time " + str(wrapped()))
    except Exception as e:  # перехват возможных ошибок
        print("[SYSTEM_LOG] function has error: " + str(e))
    finally:  # выгрузка функции из памяти
        print("[SYSTEM_LOG] function has been cleared from memory")


class Neuron:  # суперкласс для Net
    def __init__(self) -> None:  # перегрузка weight и num при конструировании
        self.weight = 0.1  # self - это замена экземпляра класса
        self.num = 0.1  # присвоение начальных значений

    def sigmoid(self) -> float:  # стандартное поведение
        return 1 / (1 + math.exp(-self.num))  # вызов функции библиотеки math с аргументом -num


class Net(Neuron):  # специализированных подкласс, наследование от Neuron
    type_nn = ''  # объявление локальной переменной

    def set_type_nn(self, type_net):  # присвоение локальной переменной внешнего значения
        self.type_nn = type_net

    def get_type_nn(self) -> str:  # возврат переменной
        return self.type_nn

    def sigmoid(self) -> float:  # специализированное поведение
        return 1 / (1 + numpy.exp(-self.num))  # вызов функции библиотеки math с аргументом -num


@logging
def print_hi(name="coder") -> None:  # функция с аргументом
    print(f'Hi, {name}')  # f - строка с передачей переменных


@logging
def arch_oop() -> None:
    perceptron1 = Net()  # экземпляр класса Net
    perceptron1.set_type_nn('perceptron')  # установка значения для типа нейронки
    print(perceptron1.type_nn)  # обращение к свойству экземпляра класса
    print('weight:', perceptron1.weight)
    print('num:', perceptron1.num)
    print('sigmoid num:', perceptron1.sigmoid())  # вызов специальной функции

    # or
    # for x in [perceptron1.type_nn,  perceptron1.weight, perceptron1.num]:
    #     print(x)


if __name__ == '__main__':  # если запускают напрямую этот файл
    try:
        print_hi('PyCharm')  # вызов функции с передачей ей аргумента
        arch_oop()  # вызов функции без аргументов
    except TypeError:  # перехват ошибки типа
        print('WARNING TypeError')

