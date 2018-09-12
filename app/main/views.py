from flask import render_template,request,redirect,url_for,abort
from ..models import  User
from . import main
from flask_login import login_required


@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "Welcome to  your best Pitches || pitch it now !"
    return render_template('index.html', title = title)


@main.route('/pitch')
def pitch():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch'
    return render_template('pitch.html', title =title)


@main.route('/category')
def category():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'pitch ||Category'
    return render_template('category.html', title = title )


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile.html", user = user)



