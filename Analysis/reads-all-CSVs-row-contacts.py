import pandas as pd
import os

directory = '/home/farzin/Projects/01-V74Q/Contacts-all-residue/contacts_chain_A'

results = []

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)

        # Get the column names for the residue contacts (excluding 'Frame.#' columns)
        residue_columns = [col for col in df.columns if not col.startswith('Frame.')]

        file_counts = {'Filename': filename}

        # Count the number of non-zero values for each column in the current file
        for column in residue_columns:
            non_zero_count = (df[column] != 0).sum()
            file_counts[column] = non_zero_count

        results.append(file_counts)


results_df = pd.DataFrame(results)

results_df.to_csv('counts_results-Q-chainA.csv', index=False, columns=residue_columns.insert(0, 'Filename'))

