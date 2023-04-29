import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def normalize_array(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    return [(x - arr_min) / (arr_max - arr_min) for x in arr]

class Tc_PPMS_Data:
    def __init__(self, pfad):
        # Öffne die Datei
        with open(pfad, 'r') as f:
            # Lese die ersten 9 Zeilen und speichere die Informationen in Klassenvariablen
            self.sample_name = f.readline().strip().split(': ')[1]
            self.voltage = float(f.readline().strip().split(': ')[1].strip(' V'))
            self.frequency = float(f.readline().strip().split(': ')[1].strip(' hz'))
            self.magnetic_field = float(f.readline().strip().split(': ')[1].strip(' mT'))
            self.starting_temperature = float(f.readline().strip().split(': ')[1].strip(' K'))
            self.ending_temperature = float(f.readline().strip().split(': ')[1].strip(' K'))
            self.temperature_rate = float(f.readline().strip().split(': ')[1].strip(' K/min'))
            self.harmonic_wave = int(f.readline().strip().split(': ')[1])
            self.coil_angle = float(f.readline().strip().split(': ')[1].strip(' degrees'))
            # Lese die Messdaten ab Zeile 10 und speichere sie als numpy-Arrays
            data = np.loadtxt(f, skiprows=1)
            self.temperature = data[:, 0]
            self.user_temp = data[:, 1]
            self.voltage = data[:, 2]
            self.voltage_mod = self.modify_array(self.voltage)
            self.dvoltage = []
            self.phase = data[:, 3]
            self.filename = pfad


    
    def modify_array(self, arr):
        # find the index of the minimum value in the array
        min_index = np.argmin(arr)
        
        # loop through the array and modify each value
        for i in range(len(arr)):
            if i < min_index:
                arr[i] -= 2 * abs(arr[min_index] - arr[i])
            else:
                pass
        return arr
            

            
    def sigmoid(self, x, a, b, c, d):
        return a + b/(1 + np.exp(-c*(x-d)))
    

    def modified_sigmoid(self,x, A, B, C, D, E, F, k):
        return A - B / (1 + np.exp(-k*(x-C))) - D / (1 + np.exp(k*(x-E))) + F


    def plot_voltage_temperature(self):
        # Create a new figure and axis object
        fig, ax = plt.subplots()

        # Add a line plot of voltage vs. temperature
        ax.plot(self.temperature, self.voltage)

        # Set the axis labels and title
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Voltage (V)')
        ax.set_title('Voltage vs. Temperature')

        # Display the plot
        plt.show()

    def plot_phase_temperature(self):
        # Create a new figure and axis object
        fig, ax = plt.subplots()

        # Add a line plot of voltage vs. temperature
        ax.plot(self.temperature, self.phase)

        # Set the axis labels and title
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Phase (deg)')
        ax.set_title('Phase vs. Temperature')

        # Display the plot
        plt.show()


    def plot_phase_voltage_temperature(self):
        # Create a new figure and axis object
        fig, ax = plt.subplots()

        # Add a line plot of voltage vs. temperature
        ax.plot(self.temperature, normalize_array(self.phase))
        ax.plot(self.temperature, normalize_array(self.voltage))

        # Set the axis labels and title
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Voltage (V)/Phase (deg)')
        ax.set_title('Voltage + Phase vs. Temperature')

        # Display the plot
        plt.show()

    def plot_dV(self):
        plt.plot(self.temperature, self.voltage)
        plt.xlabel('Temperature (K)')
        plt.ylabel('Voltage (V)')
        plt.title('Voltage vs Temperature')
        
        # Calculate the derivative using numpy's gradient function
        dVdT = np.gradient(self.voltage, self.temperature)
        # Plot the derivative in red and with a dashed line
        plt.plot(self.temperature, dVdT, 'r--', label='dV/dT')
        
        plt.legend()
        plt.show()


    def plot_fit_V(self):
        # Plot voltage vs temperature data
        fig, ax = plt.subplots(num=self.filename)

        ax.plot(self.temperature, self.voltage, 'o', label='Voltage')

        # Fit sigmoid function to data
        popt, pcov = curve_fit(self.sigmoid, self.temperature, self.voltage, [1,1,1,90])
        x_fit = np.linspace(min(self.temperature), max(self.temperature), 1000)
        y_fit = self.sigmoid(x_fit, *popt)
        ax.plot(x_fit, y_fit, label='Fit')

        # Set axis labels and legend
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Voltage (V)')
        ax.set_title(f"Tc (fit) = {popt[3]:.2f}")
        ax.legend()

        # Print fit parameters
        # print('Fit parameters:')
        # print('a =', popt[0])
        # print('b =', popt[1])
        # print('c =', popt[2])
        print(f'Tc (derived from Voltage)= {popt[3]:.2f}')
        plt.show()

    def plot_fit_ph(self):
        # Plot voltage vs temperature data
        fig, ax = plt.subplots()
        ax.plot(self.temperature, self.phase, 'o', label='Phase')

        try:
            # Fit sigmoid function to data
            popt, pcov = curve_fit(self.modified_sigmoid, self.temperature, self.phase, [80,165,90,-175,91,-110,5])
            x_fit = np.linspace(min(self.temperature), max(self.temperature), 1000)
            y_fit = self.modified_sigmoid(x_fit, *popt)
            ax.plot(x_fit, y_fit, label='Fit')
            print(f'Tc (derived from Phase) = {popt[4]:.2f}')

        except:
            print("Modified Sigmoid Fit failed")
            pass
        # Set axis labels and legend
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Voltage (V)')
        ax.legend()

        plt.show()

def main():
    import os

    folder_path = os.getcwd()  # replace with the path to your folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                print(file_path)
                messdaten = Tc_PPMS_Data(file_path)
                messdaten.plot_fit_V()
                messdaten.plot_fit_ph()

if __name__ == '__main__':
    main()