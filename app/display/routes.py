from flask import redirect,url_for,session,render_template
from app.display import display
from app.models import Upload,Comments

@display.route('/')
def show_post():
    posts = Upload.query.order_by(Upload.time.desc()).all()

    return render_template('findjobs.html',posts=posts)
