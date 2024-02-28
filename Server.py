
# from flask import Flask, render_template, request, jsonify
# from ImageProcess import preprocess_image  # Assuming ImageProcess contains preprocess_image function
# import os

# app = Flask(__name__, template_folder='./templates')
# @app.route('/', methods=['GET'])
# def hello():
#     return jsonify({'message': 'Hello, World!'})

# @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     if request.method == 'POST':
#         data=request.json
#         base64_image=data.get('base64Image')
#         # Check if the POST request has the file part
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'})

#         file = request.files['file']

#         # If the user does not select a file, the browser may send an empty file
#         if file.filename == '':
#             return jsonify({'error': 'No selected file'})

#         # Save the file to the 'images' folder
#         upload_folder = 'images'
#         if not os.path.exists(upload_folder):
#             os.makedirs(upload_folder)

#         file_path = os.path.join(upload_folder, file.filename)
#         file.save(file_path)

#         # Apply preprocessing to the uploaded image
#         processed_image_path = preprocess_image(file_path)

#         # Pass the processed image path to the HTML template
#         return render_template('upload.html', processed_image_path=processed_image_path)
#     else:
#         # Render the HTML template for GET requests without processed image
#         return render_template('upload.html', processed_image_path=None)

# if __name__ == '__main__':
#     app.run(debug=True)


















    # @app.route('/upload_image', methods=['POST'])
# def upload_image():
#     data = request.json
#     base64_image = data.get('image')

#     if base64_image:
#         # Process the base64 image and get the processed image path
#         processed_image_binary, processed_image_base64 = preprocess_image(base64_image)

#         # Respond with the processed image binary data
#         return jsonify({'success': 'true', 'image': processed_image_base64})
#     else:
#         return jsonify({'error': 'No base64 image received'})










# from flask import Flask, request, jsonify
# from flask_cors import CORS 
# app = Flask(__name__)
# CORS(app) 
# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello, World!!!'})

# @app.route('/upload_image', methods=['GET','POST'])
# def handle_data():
#     if request.method == 'POST':
#         data = request.json  # Get JSON data from the request
#         # Process the data as needed
#         print("Received data:", data)
#         # Return a response if necessary
#         return jsonify({"message": "Data received successfully"})
#     else:
#         return jsonify({"error": "Invalid request method"})

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, jsonify
# from flask_cors import CORS 

# app = Flask(__name__)
# CORS(app) 

# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello, World!!!'})

# @app.route('/upload_image', methods=['GET', 'POST'])
# def handle_data():  
#     try:
#         if request.method == 'POST':
#             data = request.json  # Get JSON data from the request
#             # Process the data as needed
#             print("Received data:", data)
#             # Return a response if necessary
#             return jsonify({"message": "Data received successfully"})
#         else:
#             return jsonify({"error": "Invalid request method"})
#     except Exception as e:
#         print("Error processing request:", str(e))
#         return jsonify({"error": "Internal server error"}), 500


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import base64
# import os

# app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def home():
#     return jsonify({'message': 'Hello, World!!!'})

# @app.route('/upload_image', methods=['POST'])
# def handle_data():
#     try:
#         if request.method == 'POST':
#             data = request.json  # Get JSON data from the request
#             base64_image = data.get('base64Image')  # Extract base64 image from data
#             if base64_image:
#                 # Process the base64 image data
#                 print("Received base64 image data")

#                 try:
#                     # Decode base64 string to bytes
#                     image_data = base64.b64decode(base64_image)

#                     # Specify the absolute or relative path to the directory
#                     save_directory = os.path.join(os.getcwd(), 'uploads')

#                     # Ensure the directory exists
#                     os.makedirs(save_directory, exist_ok=True)

#                     # Save the image to a file
#                     with open(os.path.join(save_directory, 'received_image.png'), 'wb') as img_file:
#                         img_file.write(image_data)

#                     # Return a response if necessary
#                     return jsonify({"message": "Base64 image data received successfully"})
#                 except Exception as e:
#                     print("Error decoding base64 image:", str(e))
#                     return jsonify({"error": "Error decoding base64 image"}), 500
#             else:
#                 return jsonify({"error": "No base64Image provided in the request"})
#         else:
#             return jsonify({"error": "Invalid request method"})
#     except Exception as e:
#         print("Error processing request:", str(e))
#         return jsonify({"error": "Internal server error"}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!!!'})

@app.route('/upload_image', methods=['POST'])
def handle_data():
    try:
        if request.method == 'POST':
            data = request.json  # Get JSON data from the request
            base64_image = data.get('base64Image')  # Extract base64 image from data
            if base64_image:
                # Process the base64 image data
                print("Received base64 image data")

                try:
                    # Decode base64 string to bytes
                    image_data = base64.b64decode(base64_image)

                    # Convert bytes to numpy array
                    nparr = np.frombuffer(image_data, np.uint8)

                    # Decode the image array
                    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                    # Save the image to a file in the specified directory
                    preprocess_folder = '../AI_Detect_Fake_Currency/src/screens/processedImage'
                    if not os.path.exists(preprocess_folder):
                        os.makedirs(preprocess_folder)

                    processed_image_path = os.path.join(preprocess_folder, 'processed_image.jpg')
                    cv2.imwrite(processed_image_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

                    # Return a response if necessary
                    return jsonify({"message": "Base64 image data received and saved successfully"}) 
                except Exception as e:
                    print("Error processing image:", str(e))
                    return jsonify({"error": "Error processing image"}), 500
            else:
                return jsonify({"error": "No base64Image provided in the request"})
        else:
            return jsonify({"error": "Invalid request method"})
    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

