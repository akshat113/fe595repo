# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np

def sin_graph():
    x = np.arange( 0, 2 * np.pi, 0.1)  # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    w = np.tan(x) #ff add tan function
    
    #test4535
    plt.plot(x, y, x, z, x, w)
    plt.xlabel('x values from 0 to 2pi')
    plt.ylabel('sin(x), cos(x), tan(x)') #ff update labe y axes
    plt.title('Plot of sin, cos, tan from 0 to 2pi') #ff update plot title
    plt.legend(['sin(x)', 'cos(x)', 'tan(x)']) ##ff update legend
    
    plt.axhline(y=0, color = 'black') #ff add graphical axis
    plt.axhline(y=0, color = 'black') #ff add graphical axis
    axes = plt.gca() #ff get the current Axes instance
    axes.set_ylim([-1.5 , 1.5 ]) #ff ste y axes limit
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sin_graph()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
