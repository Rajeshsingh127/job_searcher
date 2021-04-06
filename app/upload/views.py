import os
from app import app
from flask import request,abort,redirect,url_for,current_app
from flask_login import current_user
from app.upload import upload
from app.upload.forms import Uploadfeed
from werkzeug.utils import secure_filename



@upload.route('/', methods = ['POST'])
def upload_process():
        form = Uploadfeed()
        if form.validate_on_submit():
            name = request.form['name']
            about = request.form['about']
            pic = request.files['pic']
            filename = secure_filename(pic.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                    abort(400)
                pic.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
        return redirect(url_for('findjobs'))
