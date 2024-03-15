from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

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

                try:
                    # Decode base64 string to bytes
                    image_data = base64.b64decode(base64_image)

                    
                    # Save the image to a file in the same directory
                    save_path = os.path.join(os.getcwd(), 'received_image.png')
                    with open(save_path, 'wb') as img_file:
                        img_file.write(image_data)
                        print("Image saved successfully at:", save_path)

                    # Return a response if necessary
                    return jsonify({"message": "Base64 image data received successfully"}) 
                except Exception as e:
                    print("Error decoding base64 image:", str(e))
                    return jsonify({"error": "Error decoding base64 image"}), 500
            else:
                return jsonify({"error": "No base64Image provided in the request"})
        else:
            return jsonify({"error": "Invalid request method"})
    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
