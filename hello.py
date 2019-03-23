import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as pylab
import numpy as np

plt.style.use("ggplot")
params = {
            'axes.labelsize': '16',
            'xtick.labelsize': '16',
            'ytick.labelsize': '13',
            'lines.linewidth': '10',
            'legend.fontsize': '20',
            'figure.figsize': '100, 24'  # set figure size
        }
pylab.rcParams.update(params)

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.savefig("d:/filename.png", dpi=300) 




