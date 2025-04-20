import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun
from matplotlib import ticker

# Font settings for plots
font = {'family': 'serif', 'size': 15}
plt.rc('font', **font)

# Manually setting KLABELS data as per your input
group_labels = [r'$\Gamma$', 'X', 'H', 'Y', r'$\Gamma$']
xtick = [0.000, 1.058, 2.306, 3.261, 4.320]
# Load band data
Bandup = 'REFORMATTED_BAND_UP.dat'
datas_up = np.loadtxt(Bandup, dtype=np.float64)
Banddw = 'REFORMATTED_BAND_DW.dat'
datas_dw = np.loadtxt(Banddw, dtype=np.float64)

# Plot settings
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(12, 6))
for ax in [ax1, ax2, ax3, ax4]:
    ax.axhline(y=0, xmin=0, xmax=1, linestyle='--', linewidth=1, color='black')
ax4.text(4.4, 0, r"$E_F$", ha='center', va='center', fontsize=15, bbox=dict(facecolor='none', edgecolor='none'))
for i in xtick[1:-1]:
    ax2.axvline(x=i, ymin=0, ymax=1, linewidth=1.5, color='black')
    ax3.axvline(x=i, ymin=0, ymax=1, linewidth=1.5, color='black')

# Load and parse vasprun.xml for DOS data
vasprun = Vasprun('vasprun.xml', parse_dos=True)
pdos = vasprun.complete_dos.pdos
efermi = vasprun.complete_dos.efermi
energies = list(vasprun.complete_dos.energies - efermi)

# Merge PDOS data for each element
merged = {}
for site in pdos:
    data = pdos[site]
    site_str = str(site)
    atom = site_str[site_str.index("]") + 2:]
    up, down = np.zeros(len(energies)), np.zeros(len(energies))
    for orbital in data.values():
        for item in orbital.items():
            if int(item[0]) == 1:
                up += np.array(item[1])
            else:
                down -= -np.array(item[1])
    merged[atom] = [up, down]

# Define elements and colors for Cu and O
colors = ['olivedrab', 'darkcyan']  # Set colors for different elements
elements = ['Cu', 'O']  # Specify elements to plot

for i, atom in enumerate(elements):
    if atom in merged:
        ax1.plot(-merged[atom][1], energies, label=f"{atom}", color=colors[i], linewidth=1.5)
        ax1.fill_between(-merged[atom][1], energies, color=colors[i], alpha=0.5)
        ax4.fill_between(merged[atom][0], energies, color=colors[i], alpha=0.5)
        ax4.plot(merged[atom][0], energies, label=f"{atom}", color=colors[i], linewidth=1.5)

# Adjust subplot positions
pos1 = ax1.get_position()
pos4 = ax4.get_position()
pos2 = ax2.get_position()
pos3 = ax3.get_position()
ax1.set_position([pos1.x1-0.13, pos2.y0, pos3.width, pos3.height])
ax2.set_position([pos2.x1-0.163, pos2.y0, pos3.width, pos3.height])
ax4.set_position([pos4.x1-0.205, pos2.y0, pos3.width, pos3.height])

# Plot band structures
ax3.plot(datas_up[:, 0], datas_up[:, 1:], linewidth=1.0, color='darkgreen')
ax2.plot(datas_dw[:, 0], datas_dw[:, 1:], linewidth=1.0, color='darkgreen')
ax2.set_xticks(xtick)
ax2.set_xticklabels(group_labels, rotation=0, fontsize=15, fontname='serif')
ax2.grid(True, linestyle='-.')
ax2.set_xlim((xtick[0], xtick[-1]))
ax3.set_xticks(xtick)
ax3.set_xticklabels(group_labels, rotation=0, fontsize=15, fontname='serif')
ax3.grid(True, linestyle='-.')
ax3.set_xlim((xtick[-1], xtick[0]))
ax2.set_ylim(-8.5, 8.5)
ax3.set_ylim(-8.5, 8.5)
ax2.yaxis.set_major_formatter(plt.NullFormatter())
ax2.yaxis.tick_right()
ax2.tick_params(left=False, labelleft=False)
ax3.tick_params(left=True, labelleft=True)
ax1.tick_params(left=False, labelleft=False)
ax4.yaxis.set_major_formatter(plt.NullFormatter())
ax4.tick_params(left=False, labelleft=False, labelright=True)
ax1.set_xlabel("DOS")
ax4.set_xlabel("DOS")
ax1.legend()
ax1.set_ylim(-8.5, 8.5)
ax1.set_ylabel(r"$E - E_F$ (eV)")
ax4.legend()
ax4.set_ylim(-8.5, 8.5)
ax4.set_xlim(0, 4)
ax1.set_xlim(-4, 0)
xticks = ax1.get_xticks()
y_locator = ticker.MultipleLocator(1)  # Adjust step size as needed
ax2.yaxis.set_major_locator(y_locator)
ax3.yaxis.set_major_locator(y_locator)
xticks = xticks[:-1]
ax1.legend(fontsize=11).get_frame().set_alpha(0)
ax4.legend(fontsize=11).get_frame().set_alpha(0)
ax1.set_xticks(xticks)
ax4.set_xticks(ax4.get_xticks()[1:])
ax4.text(-3.06, 0.005, "a)", transform=plt.gca().transAxes, fontsize=12, va="bottom", ha="right", color="white", bbox=dict(facecolor="black", edgecolor="none", pad=2))
ax1.text(0.3, 0.7, "spin down", rotation=90, transform=ax1.transAxes, ha='center', va='center')
ax4.text(0.3, 0.7, "spin up", rotation=90, transform=ax4.transAxes, ha='center', va='center')
ax4.text(0.40, 0.47, r'$E_g = 2.1581 \mathrm{}$eV', transform=ax4.transAxes, ha='center', va='center', fontsize=10, fontname='serif')
ax1.text(0.40, 0.47, r'$E_g = 2.3396 \mathrm{}$eV', transform=ax1.transAxes, ha='center', va='center', fontsize=10, fontname='serif')
plt.savefig('dosband.png', bbox_inches='tight', pad_inches=0.1, dpi=200)
plt.show()
