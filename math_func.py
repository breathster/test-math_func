def reading(x):  #читает файл
    f = open(x, 'r')
    print("В файле:", end=' ')
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
    f.close()


def list_creating(x):  # составляет из чисел в файле массив
    f = open(x, "r+")
    s = (f.read())
    a = s.split(' ')
    a = [i for i in a if i != '']
    f.close()
    result = [float(i) for i in a]
    print(result)
    return result


def minimum(*x): #ищет минимальное
    if type(x[0]) == list: #если это минимальное мы ищем в файле, то есть minimum(list_creating("название.txt"))
        x = x[0]  #так как создается tuple, в котором на первом месте стоит наш массив
    else:
        x = list(x)  #это если мы просто вводим сичла minimum(1, 2, 3)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    if len(x) > 150:  #150 чисел - максимум для невозникновения аварийной ситуации
        raise ValueError('Number of figures exceeded')
    for j in range(len(x) - 1, 0, -1):
        for i in range(0, j):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    print("Минимальное:", x[0])
    return x[0]


def maximum(*x):
    if type(x[0]) == list: #тоже самое что с минимумом
        x = x[0]
    else:
        x = list(x)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    if len(x) > 150:  #150 чисел - максимум для невозникновения аварийной ситуации
        raise ValueError('Number of figures exceeded')
    for j in range(len(x) - 1, 0, -1):
        for i in range(0, j):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    print("Максимальное:", x[-1])
    return x[-1]


def add(*x):
    if type(x[0]) == list: #тоже самое что с минимумом
        x = x[0]
    else:
        x = list(x)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    if len(x) > 150:  #150 чисел - максимум для невозникновения аварийной ситуации
        raise ValueError('Number of figures exceeded')
    s = 0
    for i in x:
        s = s + i
        if s > 1000000000000000000000000000000: #если сумма в какой-то момент превысит это число, выдает ошибку, чтобы не было аварийного завершения
            raise ValueError('Too large numbers. Counting is abnormally suspended')
    print("Сумма:", s)
    return s


def mult(*x):
    if type(x[0]) == list:  # тоже самое что с минимумом
        x = x[0]
    else:
        x = list(x)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    m = 1
    if len(x) > 150:  #150 чисел - максимум в умножении, для невозникновения аварийной ситуации
        raise ValueError('Number of figures exceeded')
    for i in x:
        m = m * i
        if m > 1000000000000000000000000000000: #если произведение в какой-то момент превысит это число, выдает ошибку, чтобы не было аварийного завершения
            raise ValueError('Too large numbers. Counting is abnormally suspended')
    print("Произведение:", m)
    return m


def sorting(*x): #дополнительная функция
    if type(x[0]) == list:  # тоже самое что с минимумом
        x = x[0]
    else:
        x = list(x)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    for j in range(len(x) - 1, 0, -1):
        for i in range(0, j):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
    print("Отсортированный список:", x)
    return x


def divide(*x): #дополнительная функция
    if x[0] == 0:
        raise ZeroDivisionError("Cannot be divisible by 0")
    if type(x[0]) == list:  # тоже самое что с минимумом
        x = x[0]
    else:
        x = list(x)
    for i in range(len(x)):
        if type(x[i]) == str:
            raise ValueError("Not a number")
        float(i)
    print(f"Результат деления на {x[0]}:", end=' ')
    for i in range(len(x)):
        if i > 0:
            x[i] = x[i] / x[0]
            print(x[i], end=', ')
    return x


# sorting(list_creating("1.txt"))
divide(15, 59, 98, -3, 0.5)