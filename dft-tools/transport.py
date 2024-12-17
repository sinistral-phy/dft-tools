import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.core import Spin, OrbitalType
import matplotlib as mpl
from matplotlib.ticker import ScalarFormatter
from ase.units import Ry

# Set the font globally for all plots
font = {'family': 'serif', 'size': 15}
plt.rc('font', **font)

# Create the subplots
fig, axes = plt.subplots(4, 2, figsize=(12, 12), gridspec_kw={'hspace': 0.35, 'wspace': 0.2})
ax1, ax2, ax3, ax4, ax5, ax6,ax7,ax8 = axes.flatten()

# Conversion volumes
Vol_ang_Br = 271.13
Vol_Br = Vol_ang_Br * 1.0e+36
Vol_ang_Cl = 231.61
Vol_Cl = Vol_ang_Cl * 1.0e+36
Vol_ang_I = 332.82
Vol_I = Vol_ang_I * 1.0e+36

# Load and preprocess data
condtens_Br_s = np.genfromtxt('interpolation_Br.trace', skip_header=1)
Ef_Br_s = (condtens_Br_s[:, 0] * Ry)- 5.114   # Ef: Ry -> eV
Ef_Br = condtens_Br_s[:, 0]   # Ef: Ry -> eV
T_Br_s = condtens_Br_s[:, 1]  # Leave T in Kelvin
S_Br_s = condtens_Br_s[:, 4]
s_Br_s = condtens_Br_s[:, 5]
k_Br_s = condtens_Br_s[:, 7]
c_Br_s = condtens_Br_s[:, 9]

condtens_Cl_s = np.genfromtxt('interpolation_Cl.trace', skip_header=1)
Ef_Cl_s = (condtens_Cl_s[:, 0] * Ry)- 6.108924319   # Ef: Ry -> eV
Ef_Cl = condtens_Cl_s[:, 0]   # Ef: Ry -> eV
T_Cl_s = condtens_Cl_s[:, 1]  # Leave T in Kelvin
S_Cl_s = condtens_Cl_s[:, 4]
s_Cl_s = condtens_Cl_s[:, 5]
k_Cl_s = condtens_Cl_s[:, 7]
c_Cl_s = condtens_Cl_s[:, 9]

condtens_I = np.genfromtxt('interpolation_I.trace', skip_header=1)
Ef_I_s = (condtens_I[:, 0] * Ry)- 5.885082   # Ef: Ry -> eV
Ef_I = condtens_I[:, 0]   # Ef: Ry -> eV
T_I_s = condtens_I[:, 1]  # Leave T in Kelvin
S_I_s = condtens_I[:, 4]
s_I_s = condtens_I[:, 5]
k_I_s = condtens_I[:, 7]
c_I_s = condtens_I[:, 9]

# Masks for the desired temperatures
mask_Br_300 = T_Br_s == 300
mask_Br_600 = T_Br_s == 600
mask_Br_900 = T_Br_s == 900

mask_Cl_300 = T_Cl_s == 300
mask_Cl_600 = T_Cl_s == 600
mask_Cl_900 = T_Cl_s == 900

mask_I_300 = T_I_s == 300
mask_I_600 = T_I_s == 600
mask_I_900 = T_I_s == 900
ZT_Br_s = (S_Br_s )**2 * s_Br_s/k_Br_s
ZT_Cl_s = (S_Cl_s )**2 * s_Cl_s/k_Cl_s
ZT_I_s = (S_I_s )**2 * s_I_s/k_I_s
PF_Br_s = (S_Br_s )**2 * s_Br_s
PF_Cl_s = (S_Cl_s )**2 * s_Cl_s
PF_I_s = (S_I_s )**2 * s_I_s
# Plot for Br at different temperatures
ax3.plot(Ef_Br_s[mask_Br_300], 1000000 * S_Br_s[mask_Br_300], label="300 K", color='palevioletred', linewidth=2.5)
ax3.plot(Ef_Br_s[mask_Br_600], 1000000 * S_Br_s[mask_Br_600], label="600 K", color='teal', linewidth=2.5)
ax3.plot(Ef_Br_s[mask_Br_900], 1000000 * S_Br_s[mask_Br_900], label="900 K", color='firebrick', linewidth=2.5)

# Plot for Cl at different temperatures
ax1.plot(Ef_Cl_s[mask_Cl_300], 1000000 * S_Cl_s[mask_Cl_300], label="300 K", color='palevioletred', linewidth=2.5)
ax1.plot(Ef_Cl_s[mask_Cl_600], 1000000 * S_Cl_s[mask_Cl_600], label="600 K", color='teal', linewidth=2.5)
ax1.plot(Ef_Cl_s[mask_Cl_900], 1000000* S_Cl_s[mask_Cl_900], label="900 K", color='firebrick', linewidth=2.5)

# Plot for I at different temperatures
ax5.plot(Ef_I_s[mask_I_300], 1000000 * S_I_s[mask_I_300], label="300 K", color='palevioletred', linewidth=2.5)
ax5.plot(Ef_I_s[mask_I_600], 1000000 * S_I_s[mask_I_600], label="600 K", color='teal', linewidth=2.5)
ax5.plot(Ef_I_s[mask_I_900], 1000000 * S_I_s[mask_I_900], label="900 K", color='firebrick', linewidth=2.5)

# Plot Electrical Conductivity vs Temperature

# Plot Thermal Conductivity vs Temperature
mask_Br = (Ef_Br == 0.134154) & (T_Br_s > 250)
mask_Cl = (Ef_Cl == 0.157628) & (T_Cl_s > 250)
mask_I = (Ef_I == 0.430911) & (T_I_s > 250)
mask_Br_Z = (Ef_Br == 0.134154) & (T_Br_s > 450)
mask_Cl_Z = (Ef_Cl == 0.157628) & (T_Cl_s > 450)	
mask_I_Z = (Ef_I == 0.430911) & (T_I_s > 450)
ax4.plot(T_Cl_s[mask_Cl],  k_Cl_s[mask_Cl], label="Cl", color='dodgerblue', linewidth=2.5,marker="o")
ax4.plot(T_Br_s[mask_Br],  k_Br_s[mask_Br], label="Br", color='olivedrab', linewidth=2.5,marker="^")
ax4.plot(T_I_s[mask_I],  k_I_s[mask_I], label="I", color='darkslategrey', linewidth=2.5,marker="^")
ax6.plot(T_Cl_s[mask_Cl],  PF_Cl_s[mask_Cl], label="Cl", color='dodgerblue', linewidth=2.5,marker="o")
ax6.plot(T_Br_s[mask_Br],  PF_Br_s[mask_Br], label="Br", color='olivedrab', linewidth=2.5,marker="^")
ax6.plot(T_I_s[mask_I],  PF_I_s[mask_I], label="I", color='darkslategrey', linewidth=2.5,marker="^")
ax8.plot(T_Cl_s[mask_Cl_Z],  T_Cl_s[mask_Cl_Z]*ZT_Cl_s[mask_Cl_Z], label="Cl", color='dodgerblue', linewidth=2.5,marker="^")
ax8.plot(T_Br_s[mask_Br_Z],  T_Br_s[mask_Br_Z]*ZT_Br_s[mask_Br_Z], label="Br", color='olivedrab', linewidth=2.5,marker="^")
ax8.plot(T_I_s[mask_I_Z],  T_I_s[mask_I_Z]*ZT_I_s[mask_I_Z], label="I", color='darkslategrey', linewidth=2.5,marker="^")
ax2.plot(T_Cl_s[mask_Cl],  s_Cl_s[mask_Cl], label="Cl", color='dodgerblue', linewidth=2.5,marker="o")
ax2.plot(T_Br_s[mask_Br],  s_Br_s[mask_Br], label="Br", color='olivedrab', linewidth=2.5,marker="^")
ax2.plot(T_I_s[mask_I],  s_I_s[mask_I], label="I", color='darkslategrey', linewidth=2.5,marker="^")
ax7.plot(T_Cl_s[mask_Cl],  1000000*S_Cl_s[mask_Cl], label="Cl", color='palevioletred', linewidth=2.5,marker="o")
ax7.plot(T_Br_s[mask_Br],  1000000*S_Br_s[mask_Br], label="Br", color='teal', linewidth=2.5,marker="^")
ax7.plot(T_I_s[mask_I],  1000000*S_I_s[mask_I], label="I", color='firebrick', linewidth=2.5,marker="^")

# Set labels
ax4.set_xlabel("Temperature (K)")
ax1.set_ylabel("$S$ [$\\mu$V K$^{-1}$]")
ax3.set_ylabel("$S$ [$\\mu$V K$^{-1}$]")
ax5.set_ylabel("$S$ [$\\mu$V K$^{-1}$]")
ax5.set_xlabel("$\\mu - E_f$ (eV)")
ax3.set_xlabel("$\\mu - E_f$ (eV)")
ax1.set_xlabel("$\\mu - E_f$ (eV)")
ax6.set_xlabel("Temperature (K)")
ax7.set_xlabel("Temperature (K)")
ax6.set_ylabel("PF [W/K$^2$ms]")	
ax7.set_ylabel("$S$ [$\\mu$V K$^{-1}$]")	
ax8.set_ylabel("ZT")
ax4.set_ylabel("$\\kappa_e/\\tau_0$ [W/(mKs)]")
ax2.set_ylabel("$\\sigma/\\tau_0$ [$\\Omega$ m$^{-1}$s$^{-1}$]")
ax8.set_xlabel("Temperature (K)")
ax2.set_xlabel("Temperature (K)")
ax8.set_xlabel("Temperature (K)")
ax1.text(0.25, 0.9, "BaCoCl$_3$", transform=ax1.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='center')
ax3.text(0.25, 0.9, "BaCoBr$_3$", transform=ax3.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='center')
ax5.text(0.25, 0.9, "BaCoI$_3$", transform=ax5.transAxes, fontsize=18, verticalalignment='top', horizontalalignment='center')
# Apply formatting
for ax in [ax1, ax2, ax3, ax4, ax5, ax6,ax7,ax8]:
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.grid(True, linestyle='-.')

# Add legends
for ax in [ax1, ax2, ax3, ax4, ax5, ax6,ax7,ax8]:
    ax.legend(fontsize=12).get_frame().set_alpha(0)

plt.savefig("transport.png", dpi=200, bbox_inches='tight')
