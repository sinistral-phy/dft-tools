import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'

# Read the data from the file (adjust the path as needed)
data = np.loadtxt("band.dat")

# Identify the indices where rows end (separated by spaces)
row_ends = np.where(data[1:, 0] < data[:-1, 0])[0] + 1

# Create a new figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # Adjust the figure size

# Plot the band structure in the first subplot
for i in range(len(row_ends)):
    start_idx = 0 if i == 0 else row_ends[i - 1]
    end_idx = row_ends[i]
    ax1.plot(data[start_idx:end_idx, 0], data[start_idx:end_idx, 1], label=f"Dataset {i+1}")

# Read data from the file and skip lines starting with #
with open("total_dos.dat", "r") as file:
    data_lines = [line.strip() for line in file if not line.startswith("#")]

# Extract columns for DOS
column1 = []
column2 = []
for line in data_lines:
    columns = line.split()  # Assuming space-separated data
    column1.append(float(columns[0]))
    column2.append(float(columns[1]))

# Create a scatter plot for density of states in the second subplot
ax2.plot(column2, column1, color='xkcd:dark blue', label="Density of states of BaCoBr$_3$")
ax2.fill(column2, column1, color='xkcd:sky blue', alpha=0.75)

# Set labels and titles for both subplots
ax1.set_ylabel("Frequency [THz]")
ax1.set_title("Band Structure of BaCoBr$_3$")
ax1.grid(True)
ax1.set_ylim(-1.5,4.25)
ax2.set_xlabel("Density of states")
ax2.set_title("Density of States of BaCoBr$_3$")
ax2.grid(True)
ax2.set_yticklabels([])
ax2.legend()
ax2.set_ylim(-1.5,4.25)

# Adjust spacing between subplots
plt.tight_layout()

# Save the combined plot
plt.savefig("Band_DOS_BaCoBr3_side_by_side.png")

# Show the plot
plt.show()

