from flask import Flask, request, redirect, render_template, send_from_directory
import os

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure the app to use the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Get the list of uploaded files
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

# Handle file upload
@app.route('/upload', methods=['POST'])
def uploadfile():
    if 'file' not in request.files:
        return 'No file found'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected'
    
    # Save the file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    print(f"File saved to: {file_path}")
    
    return f'File uploaded: {file.filename}'

# Route to download uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
