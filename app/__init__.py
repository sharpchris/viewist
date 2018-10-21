# Import flask and template operators
from flask import Flask, json

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

