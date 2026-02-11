# Weighing Scale Display Detection

This project implements a fine-tuned object detection model designed to identify the active weighing scale display in an image. The system is trained to distinguish between a relevant display showing a weight measurement and inactive displays (showing 0.00) or background noise.

The solution utilizes the YOLOv8 architecture, optimized for accuracy on a custom dataset of weighing scale images.

## Project Overview

Key capabilities:
- Detection of LED/LCD weight displays.
- Differentiation between active (weighing) and inactive (zeroed) states.

## Repository Structure

- **Data/**: Contains the dataset configuration and sample images used for training and validation.
- **Models/**: Stores the trained model weights.
  - `best.pt`: The model checkpoint with the highest validation performance.
  - `last.pt`: The model checkpoint from the final training epoch.
- **notebook/**: Jupyter notebooks containing the training pipeline and testing script.
- **results/**: Generated output from the training process, including confusion matrices, precision-recall curves, and inference outputs.

## Technical Details

- **Model Architecture**: YOLOv8 Nano (v8n)
- **Input Resolution**: 640x640
- **Training Epochs**: 100
- **Classes**: Active Display, Inactive Display (Background)

## Installation
Ensure you have Python 3.8+ and the required dependencies installed.

```bash
pip install ultralytics