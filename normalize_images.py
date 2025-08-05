# usage: python3 normalize_images.py [input-file] [output-path]

import numpy as np
import nibabel as nib

def zscore_normalize(img_path):

    img = nib.load(img_path)
    img_data = img.get_fdata()
    img_data = np.float32(img_data)

    MP_RC = np.percentile(img_data, 99.99)  # Find the 99.99th percentile
    # min_val = np.percentile(img_data, 1)
    min_val = np.percentile(img_data, 0)
    # print(min_val)
    # min_val = img_data.min()
    # img_data[img_data <= min_val] = min_val

    img_data[img_data > MP_RC] = MP_RC

    img_data = ((img_data - min_val) * 255.0) / (MP_RC - min_val)
    img_data = np.rint(img_data).astype('int16')

    normalized_image = nib.Nifti1Image(img_data, img.affine, img.header)

    return normalized_image

import sys

input_file = sys.argv[1]
output_path = sys.argv[2]

# perform normalization
normalized_image = zscore_normalize(input_file)

# define output file name
out_fname = input_file.replace('.gz',"")
out_fname = out_fname.replace('.nii',"")
out_fname = out_fname + '_norm.nii.gz'

# Save the masked image to a new file
nib.save(normalized_image, output_path)
