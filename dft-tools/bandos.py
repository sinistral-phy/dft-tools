import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun

# Font settings for plots
font = {'family': 'serif', 'size': 15}
plt.rc('font', **font)

# Load band data for spin-up
Bandup = 'REFORMATTED_BAND_UP.dat'
datas_up = np.loadtxt(Bandup, dtype=np.float64)

# Load and parse vasprun.xml for DOS data
vasprun = Vasprun('vasprun.xml', parse_dos=True)
pdos = vasprun.complete_dos.pdos
efermi = vasprun.complete_dos.efermi
energies = list(vasprun.complete_dos.energies - efermi)

# Merge PDOS data for each element (Cu, O, and Mg)
merged = {}
for site in pdos:
    data = pdos[site]
    site_str = str(site)
    atom = site_str[site_str.index("]") + 2:]
    up, down = np.zeros(len(energies)), np.zeros(len(energies))
    for orbital in data.values():
        for item in orbital.items():
            if int(item[0]) == 1:  # Spin-up
                up += np.array(item[1])
            else:  # Spin-down
                down -= np.array(item[1])  # Negative sign convention for spin-down
    merged[atom] = [up, down]

# Define elements and colors for Cu, O, and Mg
colors = ['olivedrab', 'darkcyan', 'mediumvioletred']  # Colors for different elements
elements = ['Cu', 'O', 'Mg']  # Specify elements

# Create subplots for DOS and band structure
fig, (ax_dos, ax_band) = plt.subplots(1, 2, figsize=(10, 8), gridspec_kw={'width_ratios': [1, 2]})

# Plot DOS for spin-up and spin-down
for i, atom in enumerate(elements):
    if atom in merged:
        ax_dos.plot(merged[atom][1], energies, color=colors[i], linewidth=1.5)
        ax_dos.fill_between(merged[atom][1], energies, color=colors[i], alpha=0.5)
        ax_dos.fill_between(merged[atom][0], energies, color=colors[i], alpha=0.5)
        ax_dos.plot(merged[atom][0], energies, label=f"{atom}", color=colors[i], linewidth=1.5)

# Add text labels for "spin up" and "spin down"
ax_dos.text(-3.5, 2, "spin down", rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=13)
ax_dos.text(3.5, 2, "spin up", rotation=90, verticalalignment='center', horizontalalignment='center', fontsize=13)

# DOS plot settings
ax_dos.axhline(y=0, linestyle='--', linewidth=1, color='black')
ax_dos.set_xlabel("DOS")
ax_dos.set_ylabel(r"$E - E_F$ (eV)")
ax_dos.set_ylim(-8.5, 8.5)
ax_dos.legend()
ax_dos.set_xlim(-4, 4)

# Plot spin-up band structure
group_labels = [r'$\Gamma$', 'X', 'H', 'Y', r'$\Gamma$']
xtick = [0.000, 0.351, 0.943, 1.259, 1.792]  # Adjusted tick positions
ax_band.plot(datas_up[:, 0], datas_up[:, 1:], linewidth=1.0, color='darkgreen')

# Band structure plot settings
ax_band.axhline(y=0, linestyle='--', linewidth=1.5, color='black')
ax_band.set_xticks(xtick)
ax_band.set_xticklabels(group_labels, rotation=0, fontsize=15, fontname='serif')

# Customize grid lines
ax_band.grid(axis='x', color='black', linestyle='-', linewidth=1)
ax_band.grid(axis='y', color='gray', linestyle='-.', linewidth=1, alpha=1)

ax_band.set_xlim((xtick[0], xtick[-1]))
ax_band.set_ylim(-8.5, 8.5)
ax_band.set_xlabel("Wave Vector")
ax_band.set_ylabel(r"$E - E_F$ (eV)")

# Adjust layout and show/save plot
plt.tight_layout()
plt.savefig('dos_band_subplot_CuO_Mg.png', bbox_inches='tight', pad_inches=0.1, dpi=200)
plt.show()
