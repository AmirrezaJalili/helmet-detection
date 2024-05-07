# Helmet Detection

Welcome to the Helmet Detection repository! This project aims to detect helmets using the advanced object detection model YOLOv8 (You Only Look Once version 8). This repository contains all the necessary code, configurations, and resources to train, evaluate, and use the model for helmet detection in various scenarios.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Training the Model](#training-the-model)
- [Evaluation and Testing](#evaluation-and-testing)
- [Model Inference](#model-inference)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Helmet Detection project focuses on identifying the presence or absence of helmets in images and video streams. By leveraging the YOLOv8 model, it provides real-time and accurate helmet detection to enhance safety protocols in industrial and construction environments.

## Features

- **Real-Time Detection**: Detect helmets swiftly and accurately in real-time.
- **Scalable**: Works across diverse environments with different lighting and conditions.
- **Customizable**: Flexible to accommodate additional object classes.

## Installation

To use this project, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/amirrezajalili/helmet-detection.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd helmet-detection
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the Helmet Detection model in two ways:

1. **Image Detection**: Detect helmets in a single image.
    ```bash
    python detect_image.py --input data/test_image.jpg --output results/
    ```
2. **Video Detection**: Detect helmets in a video file or live camera feed.
    ```bash
    python detect_video.py --input data/test_video.mp4 --output results/
    ```

Refer to each script's `--help` option for additional configuration flags.

## Data Preparation

To train the YOLOv8 model effectively, prepare your data as follows:

1. **Dataset Structure**: Organize your dataset with images and corresponding annotation files (in YOLO format).
2. **Classes**: Ensure your classes file lists "helmet" as one of the objects to detect.

## Training the Model

To train the YOLOv8 model:

1. Prepare your dataset according to the data preparation guidelines.
2. Run the training script with appropriate configuration:
    ```bash
    python train.py --config config.yaml --epochs 50
    ```

## Evaluation and Testing

To evaluate the model's performance on a test dataset, use the evaluation script:

```bash
python evaluate.py --model weights/best_model.pt --test_data data/test/
