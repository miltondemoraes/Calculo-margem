import numpy as np
import calculo as clc


def reader(url):
    data = np.genfromtxt(url, delimiter=',', usecols=np.arange(2, 3), skip_header=1, invalid_raise=False)
    year = np.genfromtxt(url, delimiter=',', usecols=np.arange(0, 1), skip_header=1)

    invalid_numbers = np.isnan(data)

    data[invalid_numbers] = 0

    return data, year


def main():
    url = input('Digite o caminho: ')

    data, year = reader(url)
    interval = np.arange(np.size(year))

    value = np.copy(data)

    value_y = clc.math(value, interval)

    clc.plot(value, value_y, interval)
    clc.is_ok(value, value_y)


if __name__ == '__main__':
    main()
