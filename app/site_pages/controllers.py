# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Define the blueprint: 'site_pages', set its url prefix: view.ist/pages
site_pages = Blueprint('pages', __name__, template_folder='templates', static_folder='static')

# Set the route and accepted methods
@site_pages.route("/", methods=['GET', 'POST'])
def index():
    return render_template("site_pages/index.html")
