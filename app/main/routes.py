from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from app.main import blueprint


@blueprint.route('/')
def route_default():
    return render_template('index.html')
