## Usage:
#   python3 apply_mask.py [mask] [image-name] [output-path]

import sys
import os

import nibabel as nib
import numpy as np

# get user inputs
mask_fn = sys.argv[1] # mask
input_im = sys.argv[2] # image name
output_path = sys.argv[3]

# Get the data arrays from the images
nifti_image = nib.load(input_im)
mask_image = nib.load(mask_fn)
nifti_data = nifti_image.get_fdata()
mask_data = mask_image.get_fdata()

# Apply the binary mask to the NIfTI data
masked_data = nifti_data * mask_data

# Create a new NIfTI image with the masked data
masked_image = nib.Nifti1Image(masked_data, nifti_image.affine)

# Save the masked image to a new file
nib.save(masked_image, output_path)
