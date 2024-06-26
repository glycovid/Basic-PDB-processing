def count_atoms(pdb_file):
    atom_count = 0
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                atom_count += 1
    return atom_count

pdb_file = 'structure.pdb' # insert your filename here
num_atoms = count_atoms(pdb_file)

print("Number of atoms in the protein structure:", num_atoms)
