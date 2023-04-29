import numpy as np

def read_xrd_data(filename):
    x = []
    y = []
    
    with open(filename, 'r') as f:
        for line in f:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))

    x = np.array(x)
    y = np.array(y)
    
    return x, y