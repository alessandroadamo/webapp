from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app import db, dash_app

import dash_html_components as html
import dash_core_components as dcc

dash_app_bp = Blueprint('dash_app_blueprint', __name__)


dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])


@dash_app_bp.route('/dash_app', methods=['GET', 'POST'])
@login_required
def index():
    return dash_app.index()

