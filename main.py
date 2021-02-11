# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np


def sin_graph():
    x = np.arange(0, 2 * np.pi, 0.1)  # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    #test
    plt.plot(x, y, x, z)
    plt.xlabel('x values from 0 to 2pi')  # string must be enclosed with quotes '  '
    plt.ylabel('sin(x) and cos(x)')
    plt.title('Plot of sin and cos from 0 to 2pi')
    plt.legend(['sin(x)', 'cos(x)'])
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sin_graph()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
