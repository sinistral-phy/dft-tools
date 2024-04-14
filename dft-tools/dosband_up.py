import os
import numpy as np
import matplotlib.pyplot as plt
from pymatgen.io.vasp import Vasprun
from pymatgen.electronic_structure.core import Spin, OrbitalType
import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import font_manager
font = {'family': 'serif', 'size': 12}
plt.rc('font', **font)
bandgap='./BAND/BAND_GAP'
# Read POSCAR and extract the element
poscar='./BAND/POSCAR'
with open(poscar, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element = sixth_line.replace(" ", "")
with open(bandgap, "r") as file:
        lines = file.readlines()
        band_gap_up = lines[1].split()[3]  # Extract the value as a string
Greek_alphabets=['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta', 'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Pega']
group_labels=[];xtick=[]
klabels='./BAND/KLABELS'
with open(klabels,'r') as reader:
    lines=reader.readlines()[1:]
for i in lines:
    s=i.encode('utf-8')
    if len(s.split())==2 and not s.decode('utf-8','ignore').startswith('*'):
        klabel=str(s.decode('utf-8','ignore').split()[0])
        for j in range(len(Greek_alphabets)):
            if (klabel.find(Greek_alphabets[j].upper())>=0):
                latex_exp=r''+'$\\'+str(Greek_alphabets[j])+'$'
                klabel=klabel.replace(str(Greek_alphabets[j].upper()),str(latex_exp))
        if (klabel.find('_')>0):
           n=klabel.find('_')
           klabel=klabel[:n]+'$'+klabel[n:n+2]+'$'+klabel[n+2:]
        group_labels.append(klabel)
        xtick.append(float(s.split()[1]))
dos="./DOS/vasprun.xml"
dosrun = Vasprun(dos)
energy_levels = dosrun.tdos.energies - dosrun.efermi
total_up = dosrun.tdos.densities[Spin.up]
spd_dos = dosrun.complete_dos.get_spd_dos()
s_up = spd_dos[OrbitalType.s].densities[Spin.up]
p_up = spd_dos[OrbitalType.p].densities[Spin.up]

Bandat = './BAND/REFORMATTED_BAND_UP.dat'
datas_up = np.loadtxt(Bandat, dtype=np.float64)
folder_name=f"Plots of {element}3"
try:
    os.mkdir(folder_name)
except FileExistsError:
    print("Done")
os.chdir(folder_name)

# Create a single plot with two subplots (side by side)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot DOS
axs[1].plot(total_up, energy_levels, label="Total DOS", color="xkcd:dark grey")
axs[1].fill_betweenx(energy_levels, total_up, color="xkcd:black", alpha=0.5)
axs[1].plot(s_up, energy_levels, label="3s orbital", color="xkcd:red")
axs[1].plot(p_up, energy_levels, label="3p orbital", color="xkcd:dark green")
axs[1].grid(True, linestyle='-.')
axs[1].set_title(f"Density of States of $\\mathrm{{{element}}}₃$ (Spin UP)")
axs[1].set_xlabel("Density of States")
axs[1].set_yticklabels([])  # Remove y-axis labels for band structure plot
axs[1].legend()
axs[1].set_xlim(0, 5)

# Plot band structure
axs[0].axhline(y=0, xmin=0, xmax=1, linestyle='--', linewidth=0.5, color='0.5')
for i in xtick[1:-1]:
    axs[0].axvline(x=i, ymin=0, ymax=1, linestyle='--', linewidth=0.5, color='0.5')
axs[0].plot(datas_up[:, 0], datas_up[:, 1:], linewidth=1.0, color='black')
axs[0].set_xticks(xtick)
axs[0].set_title(f"Band Structure for $\\mathrm{{{element}}}₃$ (Spin UP)")
axs[0].set_xticklabels(group_labels, rotation=0, fontsize=font['size'] - 2, fontname=font_manager.FontProperties(family='serif').get_name())
axs[0].grid(True, linestyle='-.')
axs[0].set_xlim((xtick[0], xtick[-1]))
axs[0].set_ylabel(r"$E - E_f$ (eV)")
axs[0].set_xlabel("KPOINTS")
axs[0].set_ylim(-3, 3)
axs[0].text(3.5, 0, f"Band Gap (eV): {band_gap_up}", fontsize=12, color='xkcd:dark red', ha='center', va='center')
plt.ylim((-3, 3))

# Remove space between subplots
plt.subplots_adjust(wspace=0, hspace=0)

# Save the combined plot
plt.tight_layout()
png=f"DOSBAND_UP {element}3"
plt.savefig(png, dpi=300, bbox_inches='tight')





