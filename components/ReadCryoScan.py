import numpy as np

from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

def linearity(array_x, array_y):
    """
    This function calculates a linear regression with the x values given by array_x
    and the y values by array_y. Returns R²-value 
    
    Inputs:
    - array_x: 1D array-like object containing the x values.
    - array_y: 1D array-like object containing the y values.
    
    Returns:
    - bool:R²-value
    """
    
    # Reshape arrays to make sure they have the same shape
    array_x = np.array(array_x).reshape(-1, 1)
    array_y = np.array(array_y).reshape(-1, 1)
    
    # Fit linear regression
    model = LinearRegression().fit(array_x, array_y)
    
    # Get R²-value
    r_squared = model.score(array_x, array_y)

    return r_squared


def fit_function(array_x, array_y):
    def func(j, jc, n):
        # print(f"{x}, {A}, {B}, {n}")
        #Power law Function E = E0*(j/j_c)^n ; E0=50mV 
        voltage = 50 * (j/jc)**n
        # print(y)
        return voltage

    popt, pcov = curve_fit(func, array_x, array_y)

    B, n = popt.tolist()

    return [ B, n]

def calculate_slopes(x, y):
    slopes = []
    for i in range(len(x)):
        if i >= 2 and i <= len(x) - 3:
            x_subset = x[i-2:i+2]
            y_subset = y[i-2:i+2]
            regression = np.polyfit(x_subset, y_subset, 1)
            slope = regression[0]
            slopes.append(slope)
        else:
            if i < 2:
                slope = (y[1]-y[0])/(x[1]-x[0])
                slopes.append(slope)
            else:
                slope = (y[-1]-y[-2])/(x[-1]-x[-2])
                slopes.append(slope)
    return slopes


def find_square_root(x):
    sqrt_x = np.sqrt(x)
    if sqrt_x.is_integer():
        return [int(sqrt_x), int(sqrt_x)]
    else:
        residue = sqrt_x % 1
        if residue % 2 == 0:
            return [int(sqrt_x), int(sqrt_x)]
        else:
            print("The square root of", x, "is not an integer. Please enter a value for a and b.")
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            return [a, b]
        
class Point:
    def __init__(self):
        self.number = None
        self.position = None
        self.position_relative = None
        self.superconducting = False
        self.jc = 0
        self.n_factor = 0
        self.r_squared = 0
        self.currents = []
        self.voltages = []
        self.Dvoltages = []
        self.DDvoltages = []
        self.no_values = 0
        
        
class CryoScanReader:
    def __init__(self, file):
        # print(file)
        file1 = open(file, 'r')

        self.total_points = 0
        self.N_sc = 0
        self.max_length = 0
        self.Dmax = 0
        self.DDmax = 0
        

        self.lines = file1.readlines()
        self.metadata = self.read_metadata()
        self.data = self.read_measurements() # Array of Datapoint Data
        x, y = find_square_root(len(self.data))
        count = 0
        for y_index in range(y):
            string = ""
            for x_index in range(x):
                this_point = self.data[count]
                output = ""
                if this_point.n_factor < 1 or this_point.jc>8:
                    output="0"
                else:
                    output=f"{this_point.jc:.2f}"
                    # output=f"{this_point.number}"
                string = string + f"{output}\t"
                count += 1
            print(string)








    def read_metadata(self):
        Lines = self.lines
        Tags=[]
        Data=[]
        for line in Lines:
            if (line.find("=") != -1) :
                Tags.append(line.split("=")[0])
                Data.append(line.split("=")[1])
        metadata = [Tags, Data]
        return metadata

    def read_measurements(self):
        Lines = self.lines
        Points = []
        Position_0 = None
        def parse_coordinates(s):
            x, y = None, None
            for item in s.split(","):
                if item.startswith("X"):
                    x = float(item[1:])
                elif item.startswith("Y"):
                    y = float(item[1:])
            return (x, y)

        i=0
        for line in Lines:
            if (line.find(",J") != -1):  #Find the Point-Measurement
                newpoint = Point()
                newpoint.number = int(line.split(",J")[0].replace("P",""))
                newpoint.position = parse_coordinates(Lines[i+1]) #Read the Measurement Points coordinates
                if len(Points) == 0:
                    newpoint.position_relative = (0,0)
                    Position_0 = newpoint.position
                else:
                    dx = newpoint.position[0] - Position_0[0]
                    dy = newpoint.position[1] - Position_0[1]
                    newpoint.position_relative = (dx,dy)
                
                found_next = False
                j=0
                while not(found_next):
                    current_line = i + 4 + j 
                    element = Lines[current_line]
                    if (element.find(",J") != -1) or element == "[END]\n":
                        found_next = True

                    if found_next == False:
                        coil_factor = 2005
                        thickness = 220
                        newpoint.currents.append((float(element.split(",")[0])* coil_factor)/thickness)
                        newpoint.voltages.append(float(element.split(",")[1]))
                    j += 1
                
                #calc linearity
                newpoint.r_squared = linearity(newpoint.currents, newpoint.voltages)
                try:
                    newpoint.jc, newpoint.n_factor = fit_function(newpoint.currents,newpoint.voltages)
                except:
                    newpoint.jc, newpoint.n_factor = [np.nan, np.nan]
                newpoint.no_values = len(newpoint.currents)
                newpoint.Dvoltages = calculate_slopes(newpoint.currents,newpoint.voltages)
                newpoint.DDvoltages = calculate_slopes(newpoint.currents,newpoint.Dvoltages)

                if np.array(newpoint.Dvoltages).max() > self.Dmax:
                    self.Dmax = np.array(newpoint.Dvoltages).max()
                if np.array(newpoint.DDvoltages).max() > self.DDmax:
                    self.DDmax = np.array(newpoint.DDvoltages).max()

                Points.append(newpoint)
                # print(f"Appended Point {newpoint.number}")
            i += 1
        for point in Points:
            if len(point.currents)>self.max_length:
                self.max_length = len(point.currents)
        self.total_points = len(Points)
        return Points


if __name__ == "__main__":

    meas = CryoScanReader(r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Jc_self\YRSm2a2.csw")
    # for element in meas.data:
    #     print(element.voltages)

