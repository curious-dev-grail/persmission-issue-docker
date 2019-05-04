from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from settings import UPLOAD_DIR
import os

from flask import send_from_directory

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.isdir(UPLOAD_DIR))
            if not os.path.isdir(UPLOAD_DIR):
                os.makedirs(UPLOAD_DIR,0o777)
            file.save(os.path.join(UPLOAD_DIR, filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("home.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_DIR,
                               filename)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
