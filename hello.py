import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as pylab
import numpy as np

plt.style.use("seaborn")
params = {
            'axes.labelsize': '16',
            'xtick.labelsize': '30',
            'ytick.labelsize': '30',
            'lines.linewidth': '10',
            'legend.fontsize': '30',
            'font.size': '20',
            'xtick.major.size'    : 4        ,
            'figure.figsize': '28, 24'  # set figure size
        }
pylab.rcParams.update(params)

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.xlabel("ff", fontsize=100)
plt.savefig("d:/filename.png", dpi=90) 




