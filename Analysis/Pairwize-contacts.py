import os
import numpy as np
import pandas as pd
import MDAnalysis as mda
from MDAnalysis.analysis import contacts
from multiprocessing import Pool

def contacts_within_cutoff(u, group_a, group_b, radius=4):
    timeseries = []
    for ts in u.trajectory:
        # calculate distances between group_a and group_b
        dist = contacts.distance_array(group_a.positions, group_b.positions)
        # determine which distances <= radius
        n_contacts = contacts.contact_matrix(dist, radius).sum()
        timeseries.append([ts.frame, n_contacts])
    return np.array(timeseries)


topology = "/home/farzin/Projects/ML/AnotherHyd/2-Mdg-O2/TauRAMD/TIT-WT-O2/NewHyd-WT-O2-SR-20ns.gro"
universe = mda.Universe(topology)

# Define the atom and residue ranges for each chain
chain_A_atom_range = range(1, 3867)  # Atom numbers for Chain A
chain_A_resid_range = range(1, 265)  # Residue numbers for Chain A

chain_B_atom_range = range(3867, 12147)  # Atom numbers for Chain B
chain_B_resid_range = range(1, 537)  # Residue numbers for Chain B

# Select residues for Chain A
chain_A_selection = f"resid {' '.join(map(str, chain_A_resid_range))} and bynum {' '.join(map(str, chain_A_atom_range))}"
chain_A_residues = universe.select_atoms(chain_A_selection).residues

# Select residues for Chain B
chain_B_selection = f"resid {' '.join(map(str, chain_B_resid_range))} and bynum {' '.join(map(str, chain_B_atom_range))}"
chain_B_residues = universe.select_atoms(chain_B_selection).residues

name = [
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-1-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-2-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-3-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-4-TIT.xtc',	
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-5-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-6-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-7-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-8-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-9-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-10-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-11-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-12-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-13-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-14-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep1-pbc-fit-15-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-1-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-2-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-3-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-4-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-5-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-6-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-7-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-8-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-9-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-10-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-11-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-12-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-13-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-14-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep3-pbc-fit-15-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-1-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-2-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-3-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-4-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-5-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-6-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-7-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-8-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-9-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-10-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-11-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-12-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-13-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-14-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep4-pbc-fit-15-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-1-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-2-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-3-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-4-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-5-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-6-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-7-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-8-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-9-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-10-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-11-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-12-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-13-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-14-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep5-pbc-fit-15-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-1-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-2-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-3-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-4-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-5-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-6-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-7-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-8-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-9-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-10-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-11-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-12-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-13-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-14-TIT.xtc',
	'NewHyd-WT-O2-TauRAMD-Rep6-pbc-fit-15-TIT.xtc',
]

def calculate_contacts(index, xtc):
    u = mda.Universe(topology, xtc)
    
    sel_lig = "resname O2L"
    lig = u.select_atoms(sel_lig)
    
    con_resid_A_df = pd.DataFrame(columns=['Frame', '# Contacts_resid_A'])
    con_resid_B_df = pd.DataFrame(columns=['Frame', '# Contacts_resid_B'])
    
    for residue_A in chain_A_residues:
        con_resid_A = contacts_within_cutoff(u, lig, residue_A.atoms, radius=4)
        con_resid_A_df_temp = pd.DataFrame(con_resid_A, columns=['Frame', f'# Contacts_lig_ChainA_vs_resid_{residue_A.resid}'])
        con_resid_A_df = pd.concat([con_resid_A_df, con_resid_A_df_temp], axis=1)
    
    for residue_B in chain_B_residues:
        con_resid_B = contacts_within_cutoff(u, lig, residue_B.atoms, radius=4)
        con_resid_B_df_temp = pd.DataFrame(con_resid_B, columns=['Frame', f'# Contacts_lig_ChainB_vs_resid_{residue_B.resid}'])
        con_resid_B_df = pd.concat([con_resid_B_df, con_resid_B_df_temp], axis=1)
    
    
    os.makedirs('contacts_chain_A', exist_ok=True)
    os.makedirs('contacts_chain_B', exist_ok=True)
    
    con_resid_A_df.to_csv(f'contacts_chain_A/contacts_chain_A_{index}.csv', index=False)
    con_resid_B_df.to_csv(f'contacts_chain_B/contacts_chain_B_{index}.csv', index=False)

if __name__ == '__main__':
    with Pool(processes=20) as pool:
        pool.starmap(calculate_contacts, enumerate(name))

