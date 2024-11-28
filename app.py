import subprocess
import time

def start_ngrok():
    print("Starting ngrok...")
    ngrok_process = subprocess.Popen(["./ngrok", "http", "5000"])
    time.sleep(2)  # Allow ngrok to initialize
    try:
        ngrok_url = subprocess.check_output(
            ["curl", "-s", "http://127.0.0.1:4040/api/tunnels"]
        ).decode("utf-8")
        print(f"Ngrok URL: {ngrok_url}")
    except Exception as e:
        print("Error fetching ngrok URL:", e)
        ngrok_process.terminate()
    return ngrok_process

import os
import subprocess
import time
from flask import Flask, render_template_string, request, jsonify
import random
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Step 1: Initialize the Flask app
app = Flask(__name__)

model = load_model("sigNUrture.h5")  # Place the file in the same directory as your notebook.

IMG_SIZE = (155, 220) 

# Step 2: Updated HTML Template with Thematic Background and Selenium Panel
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signature Verification System</title>
    <style>
        /* General styling */
        body {
            font-family: 'Roboto', Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background: #f9f9f9;
            background-image: url('https://www.transparenttextures.com/patterns/cubes.png'); /* Paper-like background */
            background-repeat: repeat;
        }

        h1 {
            color: #2c3e50;
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .container {
            background: #ffffff;
            padding: 30px;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
            text-align: center;
            max-width: 500px;
            width: 100%;
            border-top: 5px solid #2980b9;  /* Blue accent for the theme */
        }

        .form-section {
            margin-bottom: 20px;
        }

        label {
            font-size: 1.1rem;
            color: #34495e;
        }

        input[type="file"] {
            display: block;
            margin: 10px auto;
            padding: 10px;
            font-size: 1rem;
            cursor: pointer;
            background-color: #ecf0f1;
            border: 2px solid #bdc3c7;
            border-radius: 5px;
        }

        input[type="file"]:hover {
            background-color: #dfe6e9;
            border-color: #2980b9;
        }

        button {
            background-color: #2980b9;
            color: #fff;
            padding: 10px 20px;
            font-size: 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }

        button:hover {
            background-color: #1d6fa5;
        }

        .result {
            margin-top: 20px;
            font-size: 1.2rem;
            padding: 10px;
            border-radius: 5px;
        }

        .success {
            color: #27ae60;
            background-color: #ecf9f0;
        }

        .error {
            color: #e74c3c;
            background-color: #fdeaea;
        }

        footer {
            position: fixed;
            bottom: 20px;
            text-align: center;
            font-size: 0.9rem;
            color: #7f8c8d;
        }

        footer a {
            color: #2980b9;
            text-decoration: none;
        }

    </style>
</head>
<body>
    <h1>Signature Verification System</h1>
    <div class="container">
        <form method="POST" enctype="multipart/form-data">
            <div class="form-section">
                <label for="signature1">Upload First Signature File:</label>
                <input type="file" name="signature1" id="signature1">
            </div>
            <div class="form-section">
                <label for="signature2">Upload Second Signature File:</label>
                <input type="file" name="signature2" id="signature2">
            </div>
            <button type="submit">Verify Signatures</button>
        </form>
        {% if result %}
        <div class="result {{ 'success' if confidence != 'N/A' else 'error' }}">
            <b>Result:</b> {{ result }}<br>
            <b>Confidence:</b> {{ confidence }}%
        </div>
        {% endif %}

        <!-- Add Selenium Test Panel -->
        <div class="form-section">
            <label for="seleniumTest">Run Selenium Test:</label>
            <button id="seleniumTest" onclick="startSeleniumTest()">Run Test</button>
        </div>

        <div class="form-section" id="seleniumLogs" style="display: none;">
            <h3>Selenium Test Logs:</h3>
            <pre id="logOutput" style="background-color: #f5f5f5; padding: 10px; border: 1px solid #ccc;"></pre>
        </div>

        <script>
            // Function to start the Selenium test and show logs
            function startSeleniumTest() {
                document.getElementById('seleniumLogs').style.display = 'block';
                let logOutput = document.getElementById('logOutput');
                logOutput.textContent = "Starting test...";

                fetch('/run_selenium_test')
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            logOutput.textContent += "\nTest Completed Successfully!";
                        } else {
                            logOutput.textContent += "\nError: " + data.message;
                        }
                    })
                    .catch(error => {
                        logOutput.textContent += "\nError: " + error;
                    });
            }
        </script>
    </div>
    <footer>
        <p>Powered by <a href="#">SignatureTech</a></p>
    </footer>
</body>
</html>
"""

# Step 3: Flask Routes
@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    if request.method == "POST":
        # Simulate Signature Verification
        file1 = request.files.get("signature1")
        file2 = request.files.get("signature2")

        if file1 and file2:
            try:
                img1 = preprocess_image(file1)
                img2 = preprocess_image(file2)

                input_data = np.stack([img1, img2], axis=0)

                predictions = model.predict(input_data)

                match_probability = predictions[0][0] * 100

                threshold = 50  
                if match_probability >= threshold:
                    result = "Signatures Match"
                else:
                    result = "Signatures Do Not Match"

                confidence = round(match_probability, 2)
            except Exception as e:
                result = f"Error processing images: {e}"
                confidence = "N/A"
        else:
            result = "Both files are required."
            confidence = "N/A"

    return render_template_string(template, result=result, confidence=confidence)

def preprocess_image(file):
    """
    Preprocess the uploaded image file for the CNN model.
    """
    image = load_img(file, target_size=IMG_SIZE)

    image = img_to_array(image)

    image = image / 255.0

    return np.expand_dims(image, axis=0)

# Step 4: Define the function to start ngrok
def start_ngrok():
    print("Starting ngrok...")
    if not os.path.exists("ngrok"):
        print("Error: ngrok binary not found in the current directory.")
        return None

    ngrok_process = subprocess.Popen(["./ngrok", "http", "5000"])
    time.sleep(3)

    try:
        response = subprocess.check_output(["curl", "-s", "http://127.0.0.1:4040/api/tunnels"])
        import json
        tunnels = json.loads(response)
        public_url = tunnels['tunnels'][0]['public_url']
        print(f" * Public URL: {public_url}")
        return ngrok_process
    except Exception as e:
        print(f"Error fetching ngrok URL: {e}")
        ngrok_process.terminate()
        return None

# Step 5: Create a new route for running Selenium test
@app.route("/run_selenium_test", methods=["GET"])
def run_selenium_test():
    try:
        # Call a function that starts the Selenium test
        run_selenium_tests()
        return jsonify({"success": True, "message": "Test completed successfully!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

def run_selenium_tests():
    # This function will execute the Selenium test case
    log_file = "selenium_test.log"  # Log file to store test output

    # Start the Selenium test script
    selenium_process = subprocess.Popen(["python3", "run_selenium_test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with open(log_file, "w") as log:
        while True:
            output = selenium_process.stdout.readline()
            if output == b"" and selenium_process.poll() is not None:
                break
            if output:
                log.write(output.decode("utf-8"))
                log.flush()

    # The process is complete; return the results (you can also handle success/failure here)
    with open(log_file, "r") as log:
        logs = log.read()

    print(logs)

# Step 6: Start the Flask app
if __name__ == "__main__":
    ngrok_process = start_ngrok()
    if ngrok_process:
        try:
            app.run(port=5000)
        finally:
            ngrok_process.terminate()
