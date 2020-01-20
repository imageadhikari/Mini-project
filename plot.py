import matplotlib.pyplot as plt
def myPlot(x,y,x_label="x",y_label="y",title="title"):
    #plotting work
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
