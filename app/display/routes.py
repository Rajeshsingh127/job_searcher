from flask import redirect,url_for,session,render_template,request
from app import db
from app.display import display
from app.models import Upload,Comments,User,Likes
from flask_login import current_user
@display.route('/')
def show_post():
    posts = Upload.query.order_by(Upload.time.desc()).all()

    return render_template('findjobs.html',posts=posts)


@display.route('/like/<postid>')
def likes(postid):
    post_id = int(postid)
    add = Upload.query.filter_by(id=post_id).first()
    check = Likes.query.filter_by(userid=current_user.id,post_id=post_id).first()
    if check is not None:
        db.session.delete(check)
        add.likes -= 1
        db.session.commit()
        return redirect(request.referrer)
    else:
        poop = Likes(userid=current_user.id, post_id=int(post_id))
        db.session.add(poop)
        add.likes += 1
        db.session.commit()
        return redirect(request.referrer)
