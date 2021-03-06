# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define the WSGI application object
app = Flask(__name__, subdomain_matching=True)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.site_pages.controllers import site_pages as site_module
from app.links.controllers import links as link_module

# Register blueprint(s)
app.register_blueprint(site_module, url_prefix='/')
app.register_blueprint(link_module, url_prefix='/')

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

