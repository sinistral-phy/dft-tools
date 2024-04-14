import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.core import Spin, OrbitalType
poscar='./BAND/POSCAR' #Read the name of the material from POSCAR file"
with open(poscar, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element = sixth_line.replace(" ", "")
font = {'family' : 'serif', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 13.0,
    }
font = {'family': 'serif', 'size': 12}
plt.rc('font', **font)
dos="./DOS/vasprun.xml"
dosrun = Vasprun(dos)
energy_levels = dosrun.tdos.energies - dosrun.efermi
total_up = dosrun.tdos.densities[Spin.up]
total_down = dosrun.tdos.densities[Spin.down]
spd_dos = dosrun.complete_dos.get_spd_dos()  # Actual spd_dos data
s_up = spd_dos[OrbitalType.s].densities[Spin.up]
p_up = spd_dos[OrbitalType.p].densities[Spin.up]
s_down = spd_dos[OrbitalType.s].densities[Spin.down]
p_down = spd_dos[OrbitalType.p].densities[Spin.down]
folder_name=f"Plots of {element}3"
try:
    os.mkdir(folder_name)
except FileExistsError:
    print("Done")
os.chdir(folder_name)
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(total_up, energy_levels, label="Total DOS", color="xkcd:dark grey")
ax.fill_betweenx(energy_levels, total_up, color="xkcd:black", alpha=0.5)
ax.plot(s_up, energy_levels, label="3s orbital", color="xkcd:red")
ax.plot(p_up, energy_levels, label="3p orbital", color="xkcd:dark green")
ax.grid(True, linestyle='-.')
ax.set_xlabel("Density of States")
ax.set_ylabel(r"$E - E_f$ (eV)")
ax.set_title(f"Density of States of $\\mathrm{{{element}}}₃$ (Spin UP)")
ax.legend()
plt.rcParams['font.family'] = 'serif'
ax.set_ylim(-3, 3)
ax.set_xlim(0, 5)
# Show the plot
dosup=f"DOS_UP {element}3.png"
plt.savefig(dosup, dpi=300, bbox_inches="tight")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(total_down, energy_levels, label="Total DOS", color="xkcd:black")
ax.fill_betweenx(energy_levels, total_down, color="xkcd:dark purple", alpha=0.5)
ax.plot(s_down, energy_levels, label="3s orbital", color="xkcd:brown")
ax.plot(p_down, energy_levels, label="3p orbital", color="xkcd:dark pink")
ax.grid(True, linestyle='-.')
# Customize plot settings
ax.set_xlabel("Density of States")
ax.set_ylabel(r"$E - E_f$ (eV)")
ax.set_title(f"Density of States of $\\mathrm{{{element}}}₃$ (Spin DOWN)")
ax.legend()
plt.rcParams['font.family'] = 'serif'
# Set y-axis range from -3 to 3
ax.set_ylim(-3, 3)
ax.set_xlim(0, 5)
# Show the plot
dosdw=f"DOS_down {element}3.png"
plt.savefig(dosdw, dpi=300, bbox_inches="tight")
#Reference:https://plotly.com/python/v3/ipython-notebooks/density-of-states/

