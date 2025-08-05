# CaPTk radiomic feature extraction

Flywheel gear that implements CaPTk's application for single-subject [radiomic feature extraction](https://cbica.github.io/CaPTk/ht_FeatureExtraction.html). Gear will output a CSV file with the subject's radiomic features within the tumor mask, for all of the input scans.

NOTE: input images must be co-registered

Normalization (to range 0-255) is an optional step.

## Dependencies:
- CaPTk (gear uses the existing Docker container 2021.03.29)

## Required inputs:
- Tumor segmentation mask (gear automatically binarizes input mask - all non-zero voxels become 1)

## Optional inputs:
- T1
- T1CE
- T2
- FLAIR
- ADC
- Radiomic feature parameter file (if not specified, gear will use CaPTk's default 3D parameters)
- brain mask (for normalization step)

## Optional configuration:
- subject label to use in the output file
- output file name (defaults to radiomic_features.csv)
- perform normalization (for T1/T1CE/T2/FLAIR inputs)
- use intersection of tumor segmentation & brain mask during normalization

## Version history
0.1.0
    - Added optional normalization step with associated configurations