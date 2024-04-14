These tools generate plots for essential data obtained from VASP calculations

Electronic properties:
For the purpose of DOS or Band plot, it is necessary to copy the relevant files (dosband,Dos,band) to the directory associated with the experimental material. After VASPKIT has completed its execution, proceed to run the relevant programs.

Optical properties:
In the context of optical plots, it is crucial to adjust the directory paths within the code to match the location of your specific material data. The optical.py program currently accounts for four distinct materials; however, you should modify these material references accordingly.
 
Elastic Properties:
To visualize the elastic properties, execute the elasticplot script in a Python environment i.e., launch Python in the terminal and then replicate the commands specified within the elasticplot file. It is crucial to adjust the tensor_string parameter based on the calculated ‘Stiffness Tensor’ from the computation of mechanical properties using VASP. Additionally, ensure that you modify the plot title to reflect the material’s name.
