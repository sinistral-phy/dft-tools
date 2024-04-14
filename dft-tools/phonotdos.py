import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'serif'

# Read data from the file and skip lines starting with #
with open("total_dos.dat", "r") as file:
    data_lines = [line.strip() for line in file if not line.startswith("#")]

# Extract columns
column1 = []
column2 = []
for line in data_lines:
    columns = line.split()  # Assuming space-separated data
    column1.append(float(columns[0]))
    column2.append(float(columns[1]))

# Create a scatter plot
plt.plot(column1, column2, color='xkcd:dark blue', label="Density of states of BaCoBr$_3$")
plt.fill(column1, column2, color='xkcd:sky blue', alpha=0.75)
plt.xlabel("Frequency")
plt.ylabel("Density of states")
plt.title("Density of states of BaCoBr$_3$")
plt.grid(True)
plt.legend()
plt.savefig("Density_freq_BaCoBr3.png")
plt.show()

