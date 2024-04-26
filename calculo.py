import numpy as np
import matplotlib.pyplot as plt


def plot(data, equation, interval):
    plt.plot(interval, data, color='red')
    plt.plot(interval, equation)
    plt.legend(['Realidade', 'Ideal', 'AAA'])
    plt.xlabel('Período')
    plt.ylabel('Dado analisado')
    plt.title('Gráfico')
    plt.ylim(min(data) - max(interval), max(data) + max(interval))
    plt.show()


def discover(data, equation):
    more_less = np.array([])

    for i in range(len(equation)):
        if data[i] > equation[i] * 1.1:
            more_less = np.append(more_less, True)
        else:
            more_less = np.append(more_less, False)

    return more_less


def is_ok(data, equation):
    result = np.allclose(data, equation, rtol=0.1)

    if result:
        print('Valor dentro da margem')

    else:
        more_less = discover(data, equation)

        if all(not elemento for elemento in more_less):
            print('Valor dentro da margem')
        else:
            print('Valor fora do padrão')


def math(data, interval):
    numerator = (np.size(data) * np.sum(interval * data) - np.sum(interval) * np.sum(data))
    denominator = (np.size(data) * np.sum(interval**2) - np.sum(interval)**2)

    a = numerator / denominator
    b = np.mean(data) - a * np.mean(interval)

    equation = a * interval + b

    return equation

