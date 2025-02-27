"""
### Computing mordred chemical descriptors from sdf fies
"""

##Install mordred and rdkit
##try numpy version: 1.24.4 if you get something like 'cannot import name 'product' from 'numpy'

from rdkit import Chem
from mordred import Calculator, descriptors
import pandas as pd
import os


def calculate_mordred_descriptors(input_sdf_folder, output_csv):
    """
    This func calculates Mordred descriptors for all SDF files in the given folder and saves them to a CSV file.

    Parameters:
    input_sdf_folder (str): Path to the folder containing SDF files.
    output_csv (str): Path to the output CSV file.
    """
    results = []
    calc = Calculator(descriptors, ignore_3D=True)

    for file_name in os.listdir(input_sdf_folder):
        if file_name.endswith('.sdf'):
            molecule_supplier = Chem.SDMolSupplier(os.path.join(input_sdf_folder, file_name))

            for mol in molecule_supplier:
                if mol:
                    calculated_descriptors = calc(mol)
                    descriptor_data = {'FileName': file_name}
                    descriptor_data.update(calculated_descriptors.asdict())
                    results.append(descriptor_data)

    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)
    print(f"Descriptors saved to {output_csv}")

# Example usage:
calculate_mordred_descriptors('/path-to-folder-with-sdf-files/','/path-to-csv/mordred_descriptors_out.csv/')