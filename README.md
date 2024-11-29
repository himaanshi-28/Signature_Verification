# Signature Verification using CNN

## 📜 **Overview**

This project demonstrates the use of Convolutional Neural Networks (CNN) to verify handwritten signatures. The system distinguishes between genuine and forged signatures by learning the spatial and structural features of handwritten inputs. This solution is aimed at improving signature verification accuracy in fields like banking, authentication systems, and document verification.

## 🧠 **Key Features**

**Automated Verification:** Reduces manual effort in identifying forged signatures.

**Deep Learning Model:** Leverages CNN for extracting robust features from signature images.

**Binary Classification:** Determines if the given signature is genuine or forged.

**Custom Dataset Compatibility:** Works with custom datasets after preprocessing.

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

-> The model optimizes on a contrastive loss function using Adam optimizer.

**Evaluation:**

Accuracy and loss metrics are used for evaluation.

## 🖼️ **Dataset**
The dataset consists of:

Training Data: 30 unique signatories, each with 24 original (genuine) signatures and 24 forged signatures (1440 images in total).

Testing Data: 20 unique signatories, each with 24 original (genuine) signatures and 24 forged signatures (960 images in total).

**Genuine Signatures**

**Forged Signatures**

## 📊 **Results**

The model achieved:

**Training Accuracy:** 99.79%

**Testing Accuracy:** 91.83%

**Graphical Outputs:** Accuracy vs. Epochs & Loss vs. Epochs


