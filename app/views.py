# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from models import Account, Link

# Set the route and accepted methods
@app.route("/", methods=['GET', 'POST'])
def index():
    print ("Hello")
    return (json.dumps({'success':True}), 201, {'ContentType':'text/html'})