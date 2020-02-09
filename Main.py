import numpy as np
import matplotlib.pyplot as plt from scipy.optimize import curve_fit


#At the same time, denoting x axes as time in seconds, and y axes as corresponding temperature using the data withing these arrays:
x = np.x_No_sweating = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
y = np.y_No_sweating = [200, 400, 580, 810, 1050, 1100, 1150, 1190, 1200, 1250, 1190, 1160, 1000, 850, 600, 375, 300, 250, 200, 190]

#Since Nasa values are in Celcius need to convert temperatures from Celcius to Kelvin:
np.add(y,278.15)

#Creating bar graph representing the peak thermal data of shuttle surface; no sweating:
plt.bar(x_No_sweating, np.add(y,278.15), width = 90);

#lableling the axes:
plt.title("Thermal data no sweating", color = 'red')
plt.xlabel("Time (seconds)")
plt.ylabel("Temp (C)")
plt.show();

#creating fucntion to map a Poisson distribution:
def poisson(k, lamb, scale):
	return scale*(lamb**k/factorial(k))*np.exp(-lamb)
  

