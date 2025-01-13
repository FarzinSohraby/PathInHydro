import csv

input_csv_file = '/home/obiwan/Projects/Hydrogenase/ML/ValidationModels-H2-O2/ML-O2.csv'
output_csv_file = '/home/obiwan/Projects/Hydrogenase/ML/ValidationModels-H2-O2/ML-O2-norm.csv'

import csv

def process_row(row, frame_index):
    frame_value = float(row[frame_index])
    for i in range(len(row)):
        if i != frame_index:  # Skip the 5th column itself
            try:
                row_value = float(row[i])
                row[i] = row_value / frame_value
            except ValueError:
                # Skip non-numeric values
                pass

# Specify column index for the 5th column (Frame)
frame_index = 2  # Assuming 0-based indexing

with open(input_csv_file, 'r') as infile, open(output_csv_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        process_row(row, frame_index)
        writer.writerow(row)

print('Values updated and saved to', output_csv_file)

