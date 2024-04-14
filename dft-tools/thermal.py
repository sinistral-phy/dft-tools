import yaml
import matplotlib.pyplot as plt

font = {'family': 'serif', 'size': 12}
plt.rc('font', **font)

# Read data from the YAML file
with open("thermal_properties1.yaml", "r") as yaml_file1:
    data1 = yaml.safe_load(yaml_file1)
with open("thermal_properties2.yaml", "r") as yaml_file2:
    data2 = yaml.safe_load(yaml_file2)
with open("thermal_properties3.yaml", "r") as yaml_file3:
    data3 = yaml.safe_load(yaml_file3)
with open("thermal_properties4.yaml", "r") as yaml_file4:
    data4 = yaml.safe_load(yaml_file4)

# Extract relevant information
temperatures1 = []
free_energies1 = []
entropies1 = []
heat_capacities1 = []
temperatures2 = []
free_energies2 = []
entropies2 = []
heat_capacities2 = []
temperatures3 = []
free_energies3 = []
entropies3 = []
heat_capacities3 = []
temperatures4 = []
free_energies4 = []
entropies4 = []
heat_capacities4 = []

for entry in data1["thermal_properties"]:
    temperatures1.append(entry["temperature"])
    free_energies1.append(entry["free_energy"])
    entropies1.append(entry["entropy"])
    heat_capacities1.append(entry["heat_capacity"])

for entry in data2["thermal_properties"]:
    temperatures2.append(entry["temperature"])
    free_energies2.append(entry["free_energy"])
    entropies2.append(entry["entropy"])
    heat_capacities2.append(entry["heat_capacity"])

for entry in data3["thermal_properties"]:
    temperatures3.append(entry["temperature"])
    free_energies3.append(entry["free_energy"])
    entropies3.append(entry["entropy"])
    heat_capacities3.append(entry["heat_capacity"])

for entry in data4["thermal_properties"]:
    temperatures4.append(entry["temperature"])
    free_energies4.append(entry["free_energy"])
    entropies4.append(entry["entropy"])
    heat_capacities4.append(entry["heat_capacity"])

# Create separate line plots for each property
plt.figure(figsize=(10, 6))

plt.plot(temperatures1, free_energies1, label="BaCoBr$_3$", color='xkcd:red')
plt.plot(temperatures2, free_energies2, label="BaCoCl$_3$", color='xkcd:blue')
plt.plot(temperatures3, free_energies3, label="BaCoF$_3$", color='xkcd:green')
plt.plot(temperatures4, free_energies4, label="BaCoI$_3$", color='xkcd:yellow')
plt.xlabel("Temperature (K)")
plt.ylabel("Free Energy [kJ/mol]")
plt.title("Free Energy as a function of Temperature")
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig("Free_Energy.png")

plt.figure(figsize=(10, 6))
plt.plot(temperatures1, entropies1, label="BaCoBr$_3$", color='xkcd:red')
plt.plot(temperatures2, entropies2, label="BaCoCl$_3$", color='xkcd:blue')
plt.plot(temperatures3, entropies3, label="BaCoF$_3$", color='xkcd:green')
plt.plot(temperatures4, entropies4, label="BaCoI$_3$", color='xkcd:yellow')
plt.xlabel("Temperature (K)")
plt.ylabel("Entropy [J/K/mol]")
plt.title("Entropy as a function Temperature")
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig("Entropy.png")

plt.figure(figsize=(10, 6))
plt.plot(temperatures1, heat_capacities1, label="BaCoBr$_3$", color='xkcd:red')
plt.plot(temperatures2, heat_capacities2, label="BaCoCl$_3$", color='xkcd:blue')
plt.plot(temperatures3, heat_capacities3, label="BaCoF$_3$", color='xkcd:green')
plt.plot(temperatures4, heat_capacities4, label="BaCoI$_3$", color='xkcd:yellow')
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity [J/K/mol]")
plt.title("Heat Capacity as a function of Temperature")
plt.grid(True, linestyle='-.')
plt.legend()
plt.savefig("Heat_Capacity.png")
