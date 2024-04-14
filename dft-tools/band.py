import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import font_manager
font = {'family' : 'serif', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 13.0,
    }
poscar='./BAND/POSCAR'
with open(poscar, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element = sixth_line.replace(" ", "")
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
Bandup = './BAND/REFORMATTED_BAND_UP.dat'
datas_up = np.loadtxt(Bandup, dtype=np.float64)
Banddw = './BAND/REFORMATTED_BAND_DW.dat'
datas_down = np.loadtxt(Banddw, dtype=np.float64)
font = {'family': 'serif', 'size': 12}
plt.rc('font', **font)
fig_up, axe_up = plt.subplots()
axe_up.axhline(y=0, xmin=0, xmax=1, linestyle='--', linewidth=0.5, color='0.5')
for i in xtick[1:-1]:
    axe_up.axvline(x=i, ymin=0, ymax=1, linestyle='--', linewidth=0.5, color='0.5')
axe_up.plot(datas_up[:, 0], datas_up[:, 1:], linewidth=1.0, color='black')
axe_up.set_ylabel(r'$\mathrm{E}-\mathrm{E_F}$ (eV)')
axe_up.set_xticks(xtick)
axe_up.set_title(f"Band structure for $\\mathrm{{{element}}}₃$ (spin UP) ")
plt.yticks(fontsize=font['size'] - 2, fontname=font_manager.FontProperties(family='serif').get_name())
axe_up.set_xticklabels(group_labels, rotation=0, fontsize=font['size'] - 2, fontname=font_manager.FontProperties(family='serif').get_name())
axe_up.set_xlim((xtick[0], xtick[-1]))
plt.ylim((-3, 3)) 
fig_up.set_size_inches(8, 6)
folder_name=f"Plots of {element}3"
try:
    os.mkdir(folder_name)
except FileExistsError:
    print("Done")
os.chdir(folder_name)
uppng=f"band_up{element}3.png"
plt.savefig(uppng, dpi=300, bbox_inches='tight')
fig_down, axe_down = plt.subplots()
axe_down.axhline(y=0, xmin=0, xmax=1, linestyle='--', linewidth=0.5, color='0.5')
for i in xtick[1:-1]:
    axe_down.axvline(x=i, ymin=0, ymax=1, linestyle='--', linewidth=0.5, color='0.5')
axe_down.plot(datas_down[:, 0], datas_down[:, 1:], linewidth=1.0, color='black')
axe_down.set_ylabel(r'$\mathrm{E}-\mathrm{E_F}$ (eV)')
axe_down.set_xticks(xtick)
plt.yticks(fontsize=font['size'] - 2, fontname=font_manager.FontProperties(family='serif').get_name())
axe_down.set_xticklabels(group_labels, rotation=0, fontsize=font['size'] - 2, fontname=font_manager.FontProperties(family='serif').get_name())
axe_down.set_xlim((xtick[0], xtick[-1]))
axe_down.set_title(f"Band structure for $\\mathrm{{{element}}}₃$ (spin DOWN) ")
plt.ylim((-3, 3))
fig_down.set_size_inches(8, 6)
dwpng=f"band_down_{element}3.png"
plt.savefig(dwpng, dpi=300, bbox_inches='tight')

