import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pylab as pylab
import numpy as np
import csv
from matplotlib.backends.backend_pdf import PdfPages

plt.style.use("seaborn")
params = {
            'axes.labelsize': '16',
            'xtick.labelsize': '30',
            'ytick.labelsize': '30',
            'lines.linewidth': '10',
            'legend.fontsize': '30',
            'font.size': '10',
            'xtick.major.size'    : 4        ,
            'figure.figsize': '30, 24'  # set figure size
        }
d = [12,32,45,33,99,12]
o = [0,1,2,3,4,5,6]
pylab.rcParams.update(params)
zip(d)
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(d)
csvFile.close()

# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.
with PdfPages('multipage_pdf.pdf') as pdf:

    x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.title('Page One')
    plt.xlabel("ff", fontsize=100)
    pdf.savefig()
    plt.close()





