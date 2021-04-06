import os
from app import app,Upload,db
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

            address = os.path.abspath(filename)
            #saving in db part
            user = Upload(name=name,about=about,pic=address,author=current_user)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('findjobs'))
