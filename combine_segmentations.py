# usage: python3 combine_segmentations.py [seg_file_1] [seg_file_2] [output_path]

import nibabel as nib
import numpy as np

def add_binary_nifti_images(image1_path, image2_path, output_path):
    # Load NIfTI images
    image1 = nib.load(image1_path)
    image2 = nib.load(image2_path)

    # Extract data arrays
    data1 = image1.get_fdata()
    data2 = image2.get_fdata()

    # Perform addition
    result_data = np.add(data1, data2)

    # Create a new NIfTI image with the result
    result_image = nib.Nifti1Image(result_data, affine=image1.affine)

    # Save the result to a new file
    nib.save(result_image, output_path)

import sys

file_one = sys.argv[1]
file_two = sys.argv[2]
output_path = sys.argv[3]

# Save the masked image to a new file
add_binary_nifti_images(file_one, file_two, output_path)
