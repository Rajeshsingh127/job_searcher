from flask import redirect,url_for,session,render_template,request
from flask_login import current_user,login_required
from app import db
from app.profile import profile
from app.models import Upload,Comments,User
from werkzeug.security import check_password_hash



@profile.route('/')
@login_required
def display_profile():
    user = current_user
    if user is not None:
        return render_template('userprofile.html',user=user)

@profile.route('/edit')
@login_required
def edit_account():
    user = current_user
    if user is not None:
        return render_template('userprofile.html',user=user)


@profile.route('/deleteaccount')
@login_required
def delete_account():

    user = current_user
    if user is not None:
      return render_template('confirm.html')




@profile.route('/confirmdelete',methods=['POST'])
@login_required
def delete():
    if  request.method == 'POST' and check_password_hash(current_user.password, request.form['password_confirm']):
        db.session.delete(current_user)
        return redirect(url_for('display.show_post'))
    else:
        return redirect(url_for('profile.delete_account'))





@profile.route('/profile_view/<author>')
@login_required
def profile_view(author):
    user = User.query.filter_by(id=author).first()
    if user is not None:
        return render_template('userprofile.html',user=user)

