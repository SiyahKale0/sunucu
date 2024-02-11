from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Yüklenen dosyaların saklanacağı dizin
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return ' '
    file = request.files['file']
    if file.filename == '':
        return ' '
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return ' '

if __name__ == '__main__':
    app.run()
