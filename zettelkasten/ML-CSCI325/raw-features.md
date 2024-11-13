---
id: raw-features
aliases: []
tags: []
---

# Raw Features

## characteristic

raw features:

- ✓ Unmodified from source
- ✓ Contains all original information
- ✓ Often high-dimensional
- ✗ Usually noisy
- ✗ May contain redundant information
- ✗ Often computationally expensive

Processed Features:

- ✓ Cleaned and normalized
- ✓ Lower dimensionality
- ✓ More efficient for ML models
- ✗ May lose some information
- ✗ Requires preprocessing time
- ✗ May introduce assumptions

## common example of raw features

### image

- pixel value (rgb)
- resolution (1920x1080)
- file size

### text

- raw character sequences
- raw bytes

### audio

- raw waveform
- raw audio bytes

### sensor data

- gps
- temperature
- time

### Digit Recognition

for example an image:
![[raw-features.png]]

Digital recognition problem:
features -> meaning of digit

typically supervised multiclass classification
