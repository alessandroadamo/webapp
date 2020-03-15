from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import db, dash_app

import dash_html_components as html

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
