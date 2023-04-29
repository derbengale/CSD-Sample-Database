import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline

from scipy.interpolate import interp1d
sl=0
nsl=0


def calculate_slopes(x, y):
    # create an interpolation function
    f = interp1d(x, y, kind='linear', bounds_error=False, fill_value='extrapolate')
    
    # calculate slopes for each x-value
    slopes = []
    for i in range(len(x)):
        if i == 0:
            # extrapolate the slope at the left edge
            slope = (f(x[1]) - f(x[0])) / (x[1] - x[0])
        elif i == len(x) - 1:
            # extrapolate the slope at the right edge
            slope = (f(x[-1]) - f(x[-2])) / (x[-1] - x[-2])
        else:
            # calculate the slope using the centered difference formula
            slope = (f(x[i+1]) - f(x[i-1])) / (x[i+1] - x[i-1])
        slopes.append(slope)
    
    return slopes

def has_letter(str):
    flag_l = False
    for i in str:
        if i.isalpha() and i != ",":
            flag_l = True
    return flag_l 

file1 = open(r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Jc_self\YRSm2a2.csw", 'r')
Lines = file1.readlines()

i=0
messungen = []
writing = False
for line in Lines:
    if line == "0.00000,0.000\n":
        # print("Neue Reihe")
        writing = True
        messreihe = [[],[]]
    
    if writing:
        if has_letter(line):
            i+1
            if len(messreihe[0])<40:
                messungen.append(messreihe)
            else:
                nsl += 1
            # print(messreihe)
            writing = False
        else:
            d = line.split(",")
            messreihe[0].append(float(d[0]))
            messreihe[1].append(float(d[1]))
            

print(len(messungen[15][0]))

for messung in messungen:
    x=np.array(messung[0])
    y=np.array(messung[1])


    slopes = calculate_slopes(x,y)
    curv = calculate_slopes(x, slopes)
    curv = np.array(curv)
    # print(slopes)
    # plt.plot(x_range,y_spl_2d(x_range))
    supraleitend = curv.max()>30000 and y.max() > 100
    # supraleitend = True
    if supraleitend:
        plt.plot(messung[0], messung[1], color = 'green')
        sl += 1
    else:
        plt.plot(messung[0], messung[1], color = 'red', alpha = 0.1)
        nsl += 1
print(f"SL,NSL,SL/NSL: [{sl},{nsl},{(sl/(nsl+sl))*100:.2f}%]")
plt.margins(0)

plt.title("IV Kurven")
plt.xlabel("Strom")
plt.ylabel("Spannung")

plt.show()
