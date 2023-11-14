import matplotlib.pyplot as plt
from math import floor, ceil


def main() -> None:
    y_list: list[float] = []
    x_list: list[float] = []

    with open ('input.dat', 'r') as input_file:
        input_file.readline()
        
        for line in input_file:
            x_el, y_el = tuple(map(float, line.split()))

            x_list.append(x_el)
            y_list.append(y_el)

    fig, ax = plt.subplots(1)
    ax.scatter(x_list, y_list)

    ax.grid()
    ax.set_title('Радиальные скорости звезды')
    ax.set_xlabel('MJD')
    ax.set_ylabel('Скорость')
    ax.set_xticks([tick for tick in range(floor(min(x_list)), ceil(max(x_list)) + 60, 50)])

    fig.set_figwidth(15)
    fig.savefig('output.png', dpi=300)
    

if __name__ == '__main__':
    main()

