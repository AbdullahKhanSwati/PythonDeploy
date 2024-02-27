
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










from flask import Flask, request, jsonify
from flask_cors import CORS 
app = Flask(__name__)
CORS(app) 
@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!!!'})

@app.route('/upload_image', methods=['GET','POST'])
def handle_data():
    if request.method == 'POST':
        data = request.json  # Get JSON data from the request
        # Process the data as needed
        print("Received data:", data)
        # Return a response if necessary
        return jsonify({"message": "Data received successfully"})
    else:
        return jsonify({"error": "Invalid request method"})

if __name__ == '__main__':
    app.run(debug=True)