import csv
import os

# Define the input directory
input_dir = 'Excel_Files'

# Define the output directory
output_dir = 'Excel_Files_Split'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop over the suject folders in the input directory
for subject_folder in os.listdir(input_dir):

    # Skip files that are not directories
    if not os.path.isdir(os.path.join(input_dir, subject_folder)):
        continue

    # Create the subject folder in the output directory if it doesn't exist
    subject_output_dir = os.path.join(output_dir, subject_folder)
    if not os.path.exists(subject_output_dir):
        os.makedirs(subject_output_dir)

    # Loop over the 3 subfolders in the subject folder
    for subfolder_name in ['BarefootExcel', 'OrthoticsExcel', 'ShoesExcel']:

        # Define the subfolder path
        subfolder_path = os.path.join(input_dir, subject_folder, subfolder_name)

        # Skip subfolders that don't exist
        if not os.path.exists(subfolder_path):
            continue

        # Create the subfolder in the subject output directory if it doesn't exist
        subfolder_output_dir = os.path.join(subject_output_dir, subfolder_name)
        if not os.path.exists(subfolder_output_dir):
            os.makedirs(subfolder_output_dir)

        # Loop over the CSV files in the subfolder
        for csv_file_name in os.listdir(subfolder_path):

            # Skip files that are not CSVs
            if not csv_file_name.endswith('.csv'):
                continue

            # Define the input and output file paths
            input_file_path = os.path.join(subfolder_path, csv_file_name)
            output_file_path1 = os.path.join(subfolder_output_dir, csv_file_name.replace('.csv', '_force.csv'))
            output_file_path2 = os.path.join(subfolder_output_dir, csv_file_name.replace('.csv', '_vicon.csv'))

            # Open the input file
            with open(input_file_path, 'r') as input_file:

                # Initialize the CSV reader
                reader = csv.reader(input_file)

                # Create the output files
                output_file1 = open(output_file_path1, 'w', newline='')
                output_file2 = open(output_file_path2, 'w', newline='')

                # Initialize the CSV writers
                writer1 = csv.writer(output_file1)
                writer2 = csv.writer(output_file2)

                # Initialize a variable to keep track of which file we're writing to
                current_writer = writer1

                # Iterate over the rows in the input file
                for row in reader:

                    # Check if the row is a blank row
                    if len(row) == 0:

                        # Switch to the second output file
                        current_writer = writer2

                    # Check if the row contains the "model outputs" text
                    elif row[0] == 'model outputs':

                        # Skip this row
                        continue

                    # Otherwise, write the row to the current output file
                    else:
                        current_writer.writerow(row)

                # Close the output files
                output_file1.close()
                output_file2.close()