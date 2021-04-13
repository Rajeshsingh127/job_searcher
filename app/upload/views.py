import os
from app import app,Upload,db
from flask import request,abort,redirect,url_for,current_app,render_template,session
from flask_login import current_user,login_required
from app.upload import upload
from app.upload.forms import Uploadfeed
from werkzeug.utils import secure_filename



@upload.route('/', methods = ['POST'])
@login_required
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
            address = '/static/images/{}'.format(filename)
            #saving in db part
            user = Upload(name=name,about=about,pic=address,author=current_user)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('display.show_post'))


@upload.route('/edit/<id>')
@login_required
def edit_post(id):
        post = Upload.query.filter_by(id=id).first()
        if post is not None and post.author.id == current_user.id:
            return render_template('editpost.html',post=post)
        abort(400)

@upload.route('/editprocess', methods = ['POST'])
@login_required
def edit_process():
    if request.method == 'POST':
            name = request.form['name']
            about = request.form['about']
            id = request.form['id']

             #saving in db part
            post = Upload.query.filter_by(id=id).first()
            if post is not None:
                post.name = name
                post.about = about
                db.session.commit()
                return redirect(url_for('display.show_post'))
            abort(400)



@upload.route('/delete/<id>')
@login_required
def delete_post(id):
        post = Upload.query.filter_by(id=id).first()
        if post is not None and post.author.id == current_user.id:
            session['deletepost'] = post.id
            return render_template('deletepost.html',post=post)

        abort(400)


@upload.route('/deleteprocess')
@login_required
def delete_process():
    yolo = session['deletepost']
    query = Upload.query.filter_by(id=yolo).first()
    if query is not None:
        db.session.delete(query)
        db.session.commit()
        session.pop('deletepost',None)
        return redirect(url_for('profile.profile_view',author=query.author.id))
    abort(400)