# CaPTk radiomic feature extraction

Flywheel gear that implements CaPTk's application for single-subject [radiomic feature extraction](https://cbica.github.io/CaPTk/ht_FeatureExtraction.html). Gear will output a CSV file with the subject's radiomic features within the tumor mask, for all of the input scans.

NOTE: input images must be co-registered & normalized.

## Dependencies:
- CaPTk (gear uses the existing Docker container 2021.03.29)

## Required inputs:
- Tumor segmentation mask (binary)

## Optional inputs:
- T1
- T1CE
- T2
- FLAIR
- ADC
- Radiomic feature parameter file (if not specified, gear will use CaPTk's default 3D parameters)

## Optional configuration:
- subject label to use in the output file
- output file name (defaults to radiomic_features.csv)
