import os
import numpy as np
import matplotlib.pyplot as plt
font = {'family': 'serif', 'size': 12}
plt.rc('font', **font)
# Load data from files (adjust filenames and locations as needed)
#There are four POSCARS each corresponding to the four elements under consideration
poscar1='/home/ikaras/VASP/BaCoBr3/SC/POSCAR'
with open(poscar1, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element1 = sixth_line.replace(" ", "")
poscar2='/home/ikaras/VASP/BaCoCl3/SC/POSCAR'
with open(poscar2, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element2 = sixth_line.replace(" ", "")
poscar3='/home/ikaras/VASP/BaCoF3/SC/POSCAR'
with open(poscar3, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element3 = sixth_line.replace(" ", "")
poscar4='/home/ikaras/VASP/BaCoI3/SC/POSCAR'
with open(poscar4, 'r') as file:
    lines = file.readlines()
    sixth_line = lines[5].strip()
element4 = sixth_line.replace(" ", "")
imag1=f'/home/ikaras/VASP/{element1}3/Optical/IMAG.in' #Reads the IMAG.in file of the first element
real1=f'/home/ikaras/VASP/{element1}3/Optical/REAL.in' #Reads the REAL.in file of the first element
imag1_data = np.loadtxt(imag1)
real1_data = np.loadtxt(real1)
energy1 = real1_data[:, 0]
e1_1 = real1_data[:, 1]
e2_1 = imag1_data[:, 1]
k1_1 = np.sqrt((np.sqrt(e1_1**2 + e2_1**2) - e1_1) / 2)
k_1 = np.sqrt((np.sqrt(e1_1**2 + e2_1**2) - e1_1))
h = 4.135668e-15
c = 2.99792458e8
lambda_val1 = ((h * c) / energy1) * 10**2
omega1 = energy1 / (h / (2 * np.pi))
absor1 = 4 * np.pi * k_1 / lambda_val1
imag2=f'/home/ikaras/VASP/{element2}3/Optical/IMAG.in'
real2=f'/home/ikaras/VASP/{element2}3/Optical/REAL.in'
imag2_data = np.loadtxt(imag2)
real2_data = np.loadtxt(real2)
energy2 = real2_data[:, 0]
e1_2 = real2_data[:, 1]
e2_2 = imag2_data[:, 1]
k1_2 = np.sqrt((np.sqrt(e1_2**2 + e2_2**2) - e1_2) / 2)
k_2 = np.sqrt((np.sqrt(e1_2**2 + e2_2**2) - e1_2))
lambda_val2 = ((h * c) / energy2) * 10**2
omega2 = energy2 / (h / (2 * np.pi))
absor2 = 4 * np.pi * k_2 / lambda_val2
imag3 = f'/home/ikaras/VASP/{element3}3/Optical/IMAG.in'
real3 = f'/home/ikaras/VASP/{element3}3/Optical/REAL.in'
imag3_data = np.loadtxt(imag3)
real3_data = np.loadtxt(real3)
energy3 = real3_data[:, 0]
e1_3 = real3_data[:, 1]
e2_3 = imag3_data[:, 1]
k1_3 = np.sqrt((np.sqrt(e1_3**2 + e2_3**2) - e1_3) / 2)
k_3 = np.sqrt((np.sqrt(e1_3**2 + e2_3**2) - e1_3))
lambda_val3 = ((h * c) / energy3) * 10**2
omega3 = energy3 / (h / (2 * np.pi))
absor3 = 4 * np.pi * k_3 / lambda_val3
imag4 = f'/home/ikaras/VASP/{element4}3/Optical/IMAG.in'
real4 = f'/home/ikaras/VASP/{element4}3/Optical/REAL.in'
imag4_data = np.loadtxt(imag4)
real4_data = np.loadtxt(real4)
energy4 = real4_data[:, 0]
e1_4 = real4_data[:, 1]
e2_4 = imag4_data[:, 1]
k1_4 = np.sqrt((np.sqrt(e1_4**2 + e2_4**2) - e1_4) / 2)
k_4 = np.sqrt((np.sqrt(e1_4**2 + e2_4**2) - e1_4))
lambda_val4 = ((h * c) / energy4) * 10**2
omega4 = energy4 / (h / (2 * np.pi))
x_nm_values1 = lambda_val1 * 1e7
x_nm_values2 = lambda_val2 * 1e7
x_nm_values3 = lambda_val3 * 1e7
x_nm_values4 = lambda_val4 * 1e7
absor4 = 4 * np.pi * k_4 / lambda_val4
folder_name="Optical plots"
try:
    os.mkdir(folder_name)
except FileExistsError:
    print("Done")
os.chdir(folder_name)
plt.figure(figsize=(10, 6))
plt.plot(energy1[(energy1 > 0) & (energy1 < 30.0)], absor1[(energy1 > 0) & (energy1 < 30.0)], label=f"{element1}3",color='xkcd:green')
plt.plot(energy2[(energy2 > 0) & (energy2 < 30.0)], absor2[(energy2 > 0) & (energy2 < 30.0)], label=f"{element2}3",color='xkcd:blue')
plt.plot(energy3[(energy3 > 0) & (energy3 < 30.0)], absor3[(energy3 > 0) & (energy3 < 30.0)], label=f"{element3}3", color='xkcd:brown')
plt.plot(energy4[(energy4 > 0) & (energy4 < 30.0)], absor4[(energy4 > 0) & (energy4 < 30.0)], label=f"{element4}3", color='xkcd:red')
plt.xlabel("Energy [eV]")
plt.ylabel("Absorption coefficient ")
plt.title(f"Absorption coefficient as a function of energy")
plt.grid(True, linestyle="-.", linewidth=0.5)
plt.legend()
plt.savefig("absorption_vs_energy.png", dpi=300, bbox_inches='tight')
plt.close()
# Plot log10(absorption coefficient) vs. energy
plt.figure(figsize=(10, 6))
plt.plot(energy1[(energy1 > 0) & (energy1 < 30.0)], np.log10(absor1[(energy1 > 0) & (energy1 < 30.0)]), label=f"{element1}3",color='xkcd:green')
plt.plot(energy2[(energy2 > 0) & (energy2 < 30.0)], np.log10(absor2[(energy2 > 0) & (energy2 < 30.0)]), label=f"{element2}3",color='xkcd:blue')
plt.plot(energy3[(energy3 > 0) & (energy3 < 30.0)], np.log10(absor3[(energy3 > 0) & (energy3 < 30.0)]), label=f"{element3}3", color='xkcd:brown')
plt.plot(energy4[(energy4 > 0) & (energy4 < 30.0)], np.log10(absor4[(energy4 > 0) & (energy4 < 30.0)]), label=f"{element4}3", color='xkcd:red')
plt.xlabel("Energy [eV]")
plt.ylabel("Log_10 absorption coefficient ")
plt.title(f"Log plot of absorption coefficient as a function of energy")
plt.grid(True, linestyle="-.", linewidth=0.5)
plt.legend()
plt.savefig("absorption_vs_energy_log10.png", dpi=300, bbox_inches='tight')
plt.close()
plt.figure(figsize=(10, 6))
plt.plot(x_nm_values1[(x_nm_values1 > 20) & (x_nm_values1 < 600)], absor3[(x_nm_values1 > 20) & (x_nm_values1 < 600)], label=f"{element1}3", color='xkcd:green')
plt.plot(x_nm_values2[(x_nm_values2 > 20) & (x_nm_values2 < 600)], absor3[(x_nm_values2 > 20) & (x_nm_values2 < 600)], label=f"{element2}3", color='xkcd:blue')
plt.plot(x_nm_values3[(x_nm_values3 > 20) & (x_nm_values3 < 600)], absor3[(x_nm_values3 > 20) & (x_nm_values3 < 600)], label=f"{element3}3", color='xkcd:brown')
plt.plot(x_nm_values4[(x_nm_values4 > 20) & (x_nm_values4 < 600)], absor4[(x_nm_values4 > 20) & (x_nm_values4 < 600)], label=f"{element4}3", color='xkcd:red')
plt.xlabel('Wavelength [nm]') 
plt.ylabel('Absorption coefficient')
plt.title(f'Absorption coefficient as a function of wavelength')
plt.legend()
plt.grid(True,linestyle='-.')
plt.savefig('absorption_vs_lambda.png', dpi=300, bbox_inches='tight')
# Create the log plot
plt.figure(figsize=(10, 6))
plt.plot(x_nm_values1[(x_nm_values1 > 50) & (x_nm_values1 < 3000 )], np.log10(absor1[(x_nm_values1 > 50 ) & (x_nm_values1 < 3000 )]), color='xkcd:green', label=f"{element1}3")
plt.plot(x_nm_values2[(x_nm_values2 > 50 ) & (x_nm_values2 < 3000 )], np.log10(absor2[(x_nm_values2 > 50) & (x_nm_values2 < 3000 )]), color='xkcd:blue', label=f"{element2}3")
plt.plot(x_nm_values3[(x_nm_values3 > 50 ) & (x_nm_values3 < 3000 )], np.log10(absor3[(x_nm_values3 > 50 ) & (x_nm_values3 < 3000 )]), color='xkcd:brown', label=f"{element3}3")
plt.plot(x_nm_values4[(x_nm_values4 > 50 ) & (x_nm_values4 < 3000 )], np.log10(absor4[(x_nm_values4 > 50 ) & (x_nm_values4 < 3000 )]), color='xkcd:red', label=f"{element4}3")
plt.xlabel('Wavelength [nm]')
plt.ylabel('Log$_{10}$ absorption coefficient [cm$^{-1}$]')
plt.title('Log plot of absorption coefficient as a function of wavelength')
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig('absorption_vs_lambda_log10.png', dpi=300, bbox_inches='tight')
loss1 = e2_1 / (e1_1**2 + e2_1**2)
loss2 = e2_2 / (e1_2**2 + e2_2**2)
loss3 = e2_3 / (e1_3**2 + e2_3**2)
loss4 = e2_4 / (e1_4**2 + e2_4**2)
# Plot loss vs. energy
plt.figure(figsize=(10, 6))
plt.plot(energy1[(energy1 > 0) & (energy1 < 30.0)], loss1[(energy1 > 0) & (energy1 < 30.0)],  color='xkcd:green', label=f"{element1}")
plt.plot(energy2[(energy2 > 0) & (energy2 < 30.0)], loss1[(energy2 > 0) & (energy2 < 30.0)],  color='xkcd:blue', label=f"{element2}")
plt.plot(energy3[(energy3 > 0) & (energy3 < 30.0)], loss3[(energy3 > 0) & (energy3 < 30.0)], color='xkcd:brown', label=f"{element3}")
plt.plot(energy4[(energy4 > 0) & (energy4 < 30.0)], loss4[(energy4 > 0) & (energy4 < 30.0)], color='xkcd:red', label=f"{element4}")
plt.xlabel('Energy [eV]')
plt.ylabel('Loss function')
plt.title(f'Loss function vs. energy ')
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig('loss_vs_energy.png', dpi=300, bbox_inches='tight')
# Plot loss vs. wavelength
# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_nm_values1[(x_nm_values1 > 20 ) & (x_nm_values1 < 150 )], loss1[(x_nm_values1 > 20 ) & (x_nm_values1 < 150 )], label=f"{element1}3", color='xkcd:green')
plt.plot(x_nm_values2[(x_nm_values2 > 20 ) & (x_nm_values2 < 150 )], loss2[(x_nm_values2 > 20 ) & (x_nm_values2 < 150 )], label=f"{element2}3", color='xkcd:blue')
plt.plot(x_nm_values3[(x_nm_values3 > 20 ) & (x_nm_values3 < 150 )], loss3[(x_nm_values3 > 20 ) & (x_nm_values3 < 150 )], label=f"{element3}3", color='xkcd:brown')
plt.plot(x_nm_values4[(x_nm_values4 > 20 ) & (x_nm_values4 < 150 )], loss4[(x_nm_values4 > 20 ) & (x_nm_values4 < 150 )], label=f"{element4}3", color='xkcd:red')
plt.xlabel('Wavelength [nm]')
plt.ylabel('Loss function')
plt.title(f'Loss function vs. wavelength')
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig('loss_vs_lambda.png', dpi=300, bbox_inches='tight')
# Write data to a file
# Calculate reflectivity
n1 = np.sqrt((np.sqrt(e1_1**2 + e2_1**2) + e1_1) / 2)
reflec1 = ((n1 - 1)**2 + k1_1**2) / ((n1 + 1)**2 + k1_1**2)
n2 = np.sqrt((np.sqrt(e1_2**2 + e2_2**2) + e1_2) / 2)
reflec2 = ((n2 - 1)**2 + k1_2**2) / ((n2 + 1)**2 + k1_2**2)
n3 = np.sqrt((np.sqrt(e1_3**2 + e2_3**2) + e1_3) / 2)
reflec3 = ((n3 - 1)**2 + k1_3**2) / ((n3 + 1)**2 + k1_3**2)

n4 = np.sqrt((np.sqrt(e1_4**2 + e2_4**2) + e1_4) / 2)
reflec4 = ((n4 - 1)**2 + k1_4**2) / ((n4 + 1)**2 + k1_4**2)

# Plot reflectivity vs. energy
plt.figure(figsize=(10, 6))
plt.plot(energy1[(energy1 > 0) & (energy1 < 35.0)], reflec1[(energy1 > 0) & (energy1 < 35.0)], label=f"{element1}3", color='xkcd:green')
plt.plot(energy2[(energy2 > 0) & (energy2 < 35.0)], reflec2[(energy2 > 0) & (energy2 < 35.0)], label=f"{element2}3", color='xkcd:blue')
plt.plot(energy3[(energy3 > 0) & (energy3 < 35.0)], reflec3[(energy3 > 0) & (energy3 < 35.0)], label=f"{element3}3", color='xkcd:brown')
plt.plot(energy4[(energy4 > 0) & (energy4 < 35.0)], reflec4[(energy4 > 0) & (energy4 < 35.0)], label=f"{element4}3", color='xkcd:red')

plt.xlabel('Energy [eV]')
plt.ylabel('Reflectivity')
plt.title(f'Reflectivity as a function of energy')
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig('reflection_vs_energy.png', dpi=300, bbox_inches='tight')
# Plot reflectivity vs. wavelength
plt.figure(figsize=(10, 6))
plt.plot(x_nm_values1[(x_nm_values1 > 20 ) & (x_nm_values1 < 500 )], reflec1[(x_nm_values1 > 20 ) & (x_nm_values1 < 500 )], color='xkcd:green', label=f"{element1}3")
plt.plot(x_nm_values3[(x_nm_values3 > 20 ) & (x_nm_values3 < 500 )], reflec3[(x_nm_values3 > 20 ) & (x_nm_values3 < 500 )], color='xkcd:brown', label=f"{element3}3")
plt.plot(x_nm_values2[(x_nm_values2 > 20 ) & (x_nm_values2 < 500 )], reflec2[(x_nm_values2 > 20 ) & (x_nm_values2 < 500)], color='xkcd:blue', label=f"{element2}3")
plt.plot(x_nm_values4[(x_nm_values4 > 20 ) & (x_nm_values4 < 500 )], reflec4[(x_nm_values4 > 20 ) & (x_nm_values4 < 500 )], color='xkcd:red', label=f"{element4}3")
plt.xlabel('Wavelength [nm]')
plt.ylabel('Reflectivity')
plt.title(f'Reflectivity as a function of wavelength')
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig(f'reflection_vs_lambda.png', dpi=300, bbox_inches='tight')
plt.plot(energy1[(energy1 > 0) & (energy1 < 100.0)], np.sqrt(energy1[(energy1 > 0) & (energy1 < 100.0)] * absor1[(energy1 > 0) & (energy1 < 100.0)]), label=f"{element1}3",color='xkcd:green')
plt.plot(energy3[(energy3 > 0) & (energy3 < 100.0)], np.sqrt(energy3[(energy3 > 0) & (energy3 < 100.0)] * absor3[(energy3 > 0) & (energy3 < 100.0)]), label=f"{element3}3", color='xkcd:brown')
plt.xlabel("Energy [eV]")
plt.ylabel("(alpha*h*nu)^0.5 (cm^-0.5)")
plt.title(f"Tauc plot")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.savefig("tauc_r0.5.png", dpi=300, bbox_inches='tight')


