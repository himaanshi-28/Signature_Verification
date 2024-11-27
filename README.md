**Signature Verification using CNN**

📜 **Overview**

This project demonstrates the use of Convolutional Neural Networks (CNN) to verify handwritten signatures. The system distinguishes between genuine and forged signatures by learning the spatial and structural features of handwritten inputs. This solution is aimed at improving signature verification accuracy in fields like banking, authentication systems, and document verification.

🧠 **Key Features**

**Automated Verification:** Reduces manual effort in identifying forged signatures.

**Deep Learning Model:** Leverages CNN for extracting robust features from signature images.

**Binary Classification:** Determines if the given signature is genuine or forged.

**Custom Dataset Compatibility:** Works with custom datasets after preprocessing.

📂 Project Structure

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
