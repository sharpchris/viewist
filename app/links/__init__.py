from flask import Blueprint, g

from app import db

links = Blueprint('link', __name__)

# Get the subdomain so that we can query the db for the account
# before handing logic off to the controllers
@links.url_value_preprocessor
def get_account_subdomain(endpoint,values):
    # The values parameter is the subdomain that is being requested
    g.account_subdomain = values
    # TODO Query the database here

# Import the controllers after account subdomain has been defined.
from . import controllers