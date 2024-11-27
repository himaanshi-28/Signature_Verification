# Signature Verification using CNN

## 📜 **Overview**

This project demonstrates the use of Convolutional Neural Networks (CNN) to verify handwritten signatures. The system distinguishes between genuine and forged signatures by learning the spatial and structural features of handwritten inputs. This solution is aimed at improving signature verification accuracy in fields like banking, authentication systems, and document verification.

## 🧠 **Key Features**

**Automated Verification:** Reduces manual effort in identifying forged signatures.

**Deep Learning Model:** Leverages CNN for extracting robust features from signature images.

**Binary Classification:** Determines if the given signature is genuine or forged.

**Custom Dataset Compatibility:** Works with custom datasets after preprocessing.

## 📂 **Project Structure**

├── data-CEDAR/

│   ├── genuine/          # Folder for genuine signature images

│   ├── forged/           # Folder for forged signature images

├── models/

│   ├── sigNUrture.h5  # Saved CNN model

├── notebooks/

│   ├── signature_verification.ipynb  # Jupyter notebook for training and testing

├── utils/

│   ├── data_preprocessing.py        # Script for preprocessing images

│   ├── model_training.py            # Script for training the CNN

├── README.md

└── requirements.txt                 # Required Python packages

## 🚀 **How It Works**

**Data Preprocessing:**

1. Resize and normalize signature images.

2. Convert images to grayscale if needed.

3. Augment the data for better model generalization.

**CNN Architecture:**

1. Input Layer: Accepts signature images.

2. Convolutional Layers: Extract spatial features of signatures.

3. Pooling Layers: Reduce dimensionality while retaining key features.

4. Fully Connected Layers: Perform classification into genuine or forged.

**Training and Validation:**

-> The dataset is split into training, validation, and testing subsets.

-> The model optimizes on a contrastive loss function using rms optimizer.

**Evaluation:**

Accuracy and loss metrics are used for evaluation.

## 🖼️ **Dataset**
The dataset consists of 28 people signatures and for each person we have 24 genuine and 24 forged signature images.We have used CEDAR dataset for training and for testing we can use custom as well.

**Genuine Signatures**

**Forged Signatures**

## 📊 **Results**

The model achieved:

**Training Accuracy:** X%

**Validation Accuracy:** Y%

**Test Accuracy:** Z%


