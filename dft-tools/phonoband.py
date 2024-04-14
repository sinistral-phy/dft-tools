import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'

# Read the data from the file (adjust the path as needed)
data = np.loadtxt("band.dat")

# Identify the indices where rows end (separated by spaces)
row_ends = np.where(data[1:, 0] < data[:-1, 0])[0] + 1

# Plot each dataset separately
for i in range(len(row_ends)):
    start_idx = 0 if i == 0 else row_ends[i - 1]
    end_idx = row_ends[i]
    plt.plot(data[start_idx:end_idx, 0], data[start_idx:end_idx, 1], label=f"Dataset {i+1}")


plt.ylabel("Frequency [THz]")
plt.title("Band structure using phonopy for BaCoBr$_3$")
plt.xlim(0, 0.5)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.savefig('Fband_BaCoBr.png')

