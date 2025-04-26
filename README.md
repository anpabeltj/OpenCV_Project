# Motion Detector Program 😎

## Overview 🎯  
A real-time motion detector using OpenCV and NumPy. Captures webcam frames, computes frame differences, applies image processing, and highlights moving regions.

## Features ✨  
- 🎥 **Custom resolution** input  
- 🔄 **Frame differencing** for motion detection  
- 🖤 **Grayscale conversion** & 🌫️ **Gaussian blur**  
- 🎛️ **Binary thresholding** & 🩹 **Dilation**  
- 🔴 **Contour detection** & drawing  
- 🪟 **Dual-window display**: “Input” vs “Output”

## Prerequisites 📋  

| Dependency          | Min Version | Documentation                                    |
|---------------------|-------------|--------------------------------------------------|
| 🐍 Python           | 3.6+        | —                                                |
| 📷 OpenCV-Python    | 4.x         | OpenCV Documentation: https://docs.opencv.org/4.x/ |
| 🧮 NumPy            | 1.17+       | NumPy Documentation: https://numpy.org/doc/       |

## Installation 🛠️  
Clone the repository:  
   ```bash
git clone https://github.com/anpabeltj/OpenCV_Project.git
```

Change the directory:
```bash
cd OpenCV_Project
```

Create the virtual environment:
```bash

python3 -m venv venv                                                                    
source venv/bin/activate
```
Run the code:
```bash
python OpenCV_Project.py
```
