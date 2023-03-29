import os
import shutil

# Define paths and folder names
input_folder = "NEW_DATA"
output_folder = "NEW_EXCEL_DATA"

print('hello world')
# Loop over all subject folders in the input folder
for subject_folder in os.listdir(input_folder):
    print(f'Extracting from {subject_folder}')
    if os.path.isdir(os.path.join(input_folder, subject_folder)):
        # Create new subject folder in output folder
        new_subject_folder = subject_folder + "_Excel"
        os.makedirs(os.path.join(output_folder, new_subject_folder), exist_ok=True)

        # Loop over all subfolders in the subject folder
        for subfolder_name in ["Barefoot", "Orthotics", "Shoes"]:
            subfolder_path = os.path.join(input_folder, subject_folder, subfolder_name)
            if os.path.isdir(subfolder_path):
                # Loop over all CSV files in the subfolder
                for filename in os.listdir(subfolder_path):
                    if filename.endswith(".csv"):
                        # Copy CSV file to appropriate Excel folder
                        output_subfolder = subfolder_name + "Excel"
                        output_folder_path = os.path.join(output_folder, new_subject_folder, output_subfolder)
                        os.makedirs(output_folder_path, exist_ok=True)
                        shutil.copy(os.path.join(subfolder_path, filename), os.path.join(output_folder_path, filename))

print('end of loop')