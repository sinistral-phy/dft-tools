import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager
from matplotlib import font_manager
from matplotlib.ticker import ScalarFormatter
font = {'family': 'serif', 'size': 15}
plt.rc('font', **font)

# Load data for Br and Co
data_dw_Cl = np.loadtxt('PDOS_Cl_DW.dat')
data_up_Cl = np.loadtxt('PDOS_Cl_UP.dat')
energy_Cl = data_dw_Cl[:, 0]

data_dw_Co = np.loadtxt('PDOS_Co_DW.dat')
data_up_Co = np.loadtxt('PDOS_Co_UP.dat')
energy_Co = data_dw_Co[:, 0]

data_dw_Ba = np.loadtxt('PDOS_Ba_DW.dat')
data_up_Ba = np.loadtxt('PDOS_Ba_UP.dat')

data = np.loadtxt("TDOS.dat")
energy = data[:, 0]
spin_up = data[:, 1]
spin_down = data[:, 2]

# Calculate sums
columns_up_p_Co = data_up_Co[:, 1]  # 3rd to 5th columns
columns_up_d_Co = data_up_Co[:, 5:10]  # 6th to 10th columns
columns_dw_p_Co = data_dw_Co[:, 1]  # 3rd to 5th columns
columns_dw_d_Co = data_dw_Co[:, 5:10]  # 6th to 10th columns
sum_up_p_Co = columns_up_p_Co  # Sum of columns 3-5
sum_up_d_Co = np.sum(columns_up_d_Co, axis=1)  # Sum of columns 6-10
sum_dw_p_Co = columns_dw_p_Co  # Sum of columns 3-5
sum_dw_d_Co = np.sum(columns_dw_d_Co, axis=1)  # Sum of columns 6-10columns_up_p_Ba = data_up[:, 2:5]  # 3rd to 5th columns
columns_up_d_Ba = data_up_Ba[:, 5:10]  # 6th to 10th columns
columns_dw_p_Ba = data_dw_Ba[:, 1]  # 3rd to 5th columns
columns_up_p_Ba = data_up_Ba[:, 1]  # 3rd to 5th columns
columns_dw_d_Ba = data_dw_Ba[:, 5:10]  # 6th to 10th columns
sum_up_p_Ba = columns_up_p_Ba  # Sum of columns 3-5
sum_up_d_Ba = np.sum(columns_up_d_Ba, axis=1)  # Sum of columns 6-10
sum_dw_p_Ba = columns_dw_p_Ba  # Sum of columns 3-5
sum_dw_d_Ba = np.sum(columns_dw_d_Ba, axis=1)  # Sum of columns 6-10
columns_up_p_Cl = data_up_Cl[:, 1]  # 3rd to 5th columns
columns_up_d_Cl = data_up_Cl[:, 2:5]  # 6th to 10th columns
columns_dw_p_Cl = data_dw_Cl[:, 1]  # 3rd to 5th columns
columns_dw_d_Cl = data_dw_Cl[:, 2:5]  # 6th to 10th columns
sum_up_p_Cl = columns_up_p_Cl  # Sum of columns 3-5
sum_up_d_Cl = np.sum(columns_up_d_Cl, axis=1)  # Sum of columns 6-10
sum_dw_p_Cl = columns_dw_p_Cl  # Sum of columns 3-5
sum_dw_d_Cl = np.sum(columns_dw_d_Cl, axis=1)  # Sum of columns 6-10

# Create subplots
fig, (ax1, ax2, ax3,ax4) = plt.subplots(4, 1, figsize=(6, 8), sharex=True, gridspec_kw={'hspace': 0})
# Plot Cl orbitals
ax1.plot(energy , spin_up, label='Total', color='black', linewidth=2)
ax1.fill_between( energy, spin_up, color='darkmagenta', alpha=0.3)
ax1.plot(energy , spin_down, color='black', linewidth=2)
ax1.fill_between(energy, spin_down, color='palevioletred', alpha=0.3)
ax1.set_ylim([-15, 15])
ax1.grid(True, linestyle='-.')
ax1.legend(loc='upper right', fontsize=13).get_frame().set_alpha(0)

ax2.plot(energy_Cl , sum_up_p_Cl, label='Cl_3s', color='teal', linewidth=2)
ax2.plot(energy_Cl , sum_up_d_Cl, label='Cl_3p', color='darkblue', linewidth=2)
ax2.plot(energy_Cl , sum_dw_p_Cl, color='teal', linewidth=2)
ax2.plot(energy_Cl , sum_dw_d_Cl, color='darkblue', linewidth=2)
ax2.set_ylim([-15, 15])
ax2.grid(True, linestyle='-.')
ax2.legend(fontsize=13).get_frame().set_alpha(0) 

# Plot Co orbitals
ax3.plot(energy_Co , sum_up_p_Co, label='Co_3s', color='palevioletred', linewidth=2)
ax3.plot(energy_Co , sum_up_d_Co, label='Co_3d', color='darkmagenta', linewidth=2)
ax3.plot(energy_Co , sum_dw_p_Co, color='palevioletred', linewidth=2)
ax3.plot(energy_Co , sum_dw_d_Co, color='darkmagenta', linewidth=2)
ax3.set_ylim([-15, 15])
ax3.grid(True, linestyle='-.')
ax3.legend(fontsize=13).get_frame().set_alpha(0) 
data_dw = np.loadtxt('PDOS_Ba_DW.dat')
data_up = np.loadtxt('PDOS_Ba_UP.dat')
energy_Ba = data_dw_Ba[:, 0]
ax4.plot(energy_Ba , sum_up_p_Ba, label='Ba_5s', color='rosybrown', linewidth=2)
ax4.plot(energy_Ba , sum_up_d_Ba, label='Ba_5d', color='brown', linewidth=2)
ax4.plot(energy_Ba , sum_dw_p_Ba, color='rosybrown', linewidth=2)
ax4.plot(energy_Ba , sum_dw_d_Ba, color='brown', linewidth=2)
ax4.legend(loc='upper right', fontsize=13).get_frame().set_alpha(0)
ax4.set_xlim([-9, 8])
ax4.set_ylim([-15, 15])
ax4.grid(True, linestyle='-.')
plt.xlabel(r'$\mathrm{\mathit{E} - \mathit{E_F}}$ (eV)')
plt.savefig("COMBTDOS.png",bbox_inches='tight', pad_inches=0.05, dpi=200)
plt.show()
