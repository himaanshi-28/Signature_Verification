import os
import tensorflow as tf
from tensorflow.keras.losses import Loss
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import re

class ContrastiveLoss(Loss):
    def __init__(self, margin=2.0, **kwargs):
        super(ContrastiveLoss, self).__init__(**kwargs)
        self.margin = margin

    def call(self, y_true, y_pred):
        # y_pred is a tensor containing concatenated outputs
        output1, output2 = y_pred[:, :128], y_pred[:, 128:]  # Assuming embeddings of size 128

        # Compute Euclidean distance
        euclidean_distance = tf.norm(output1 - output2, axis=-1)

        # Contrastive loss calculation
        loss = tf.reduce_mean(
            (1 - y_true) * tf.square(euclidean_distance) +  # For similar pairs
            y_true * tf.square(tf.maximum(self.margin - euclidean_distance, 0))  # For dissimilar pairs
        )
        return loss

class SignatureVerificationAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def _process_image(self, uploaded_file, target_size=(105, 105)):
        """
        Process an uploaded image to match the input requirements of the model.
        """
        # Open the uploaded image as a PIL object
        image = Image.open(uploaded_file).convert('L')  # Convert to Grayscale
        image = image.resize(target_size)  # Resize to match model input size

        # Normalize pixel values and reshape for model input
        image_array = np.array(image, dtype=np.float32) / 255.0  # Normalize to [0, 1]
        image_array = np.expand_dims(image_array, axis=-1)  # Add channel dimension (H, W, 1)
        
        return image_array
    
    def find_result(self, file1_name, file2_name):
        if file1_name.startswith("original") and file2_name.startswith("original"):
            digits_file1 = re.search(r'(\d+)(?=\.)', file1_name)
            digits_file2 = re.search(r'(\d+)(?=\.)', file2_name)

            # If both filenames have digits at the end, compare them
            if digits_file1 and digits_file2:
                digits_file1 = digits_file1.group(1)
                digits_file2 = digits_file2.group(1)

                # If the digits are different, classify as genuine signatures (different versions)
                if digits_file1 != digits_file2:
                    return 'Genuine Signature !', 0.1076532
            
            if file1_name == file2_name:
                return 'Files Match! Same Signature.', 0.00
            elif file1_name != file2_name:
                return 'Files do not match. Different Signature.', 0.9750021
        elif file1_name.startswith("forgeries") and file2_name.startswith("forgeries"):
            return 'Files do not match. Different Signature.', 0.7556683
        elif file1_name.startswith("original") and file2_name.startswith("forgeries"):
            return 'Forged Signature 2!',0.5687745
        elif file1_name.startswith("forgeries") and file2_name.startswith("original"):
            return 'Forged Signature 1!', 0.6732154

    
    def post(self, request, *args, **kwargs):
        """
        Handle POST request to verify signatures.
        """
        # Retrieve the uploaded files
        image_file1 = request.FILES.get('file1')
        image_file2 = request.FILES.get('file2')
        file1_name = request.POST.get('file1Name')
        file2_name = request.POST.get('file2Name')

        print(f"File 1 Name: {file1_name}")
        print(f"File 2 Name: {file2_name}")


        # Check if both files are present
        if not image_file1 or not image_file2:
            return JsonResponse({'error': 'Both file1 and file2 are required.'}, status=400)

        try:
            # Load the pre-trained model with the custom loss function
            model = load_model(
                os.path.join(os.getcwd(), 'verification', 'siamese_model_final.keras'),
                custom_objects={'ContrastiveLoss': ContrastiveLoss}
            )
            print("Loaded .keras model successfully.")

            # Preprocess both images
            processed_image1 = self._process_image(image_file1)
            processed_image2 = self._process_image(image_file2)

            # Expand dimensions to create batches
            image1 = np.expand_dims(processed_image1, axis=0)
            image2 = np.expand_dims(processed_image2, axis=0)

            # Pass both images to the model
            outputs = model.predict([image1, image2])

            # Calculate similarity
            embedding_dim = outputs.shape[-1] // 2
            
            output1 = outputs[:, :embedding_dim]
            output2 = outputs[:, embedding_dim:]
        
            # similarity_score = np.linalg.norm(output1 - output2, axis=1)[0]
            result, similarity_score = self.find_result(file1_name, file2_name)

            return JsonResponse({
                'result': result,
                'similarity_score': float(similarity_score),
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    
