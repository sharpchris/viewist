# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Define the blueprint: 'links', set its url prefix: view.ist/link
links = Blueprint('links', __name__, subdomain="<account>")

# Import module models (i.e. User)
from app.links.models import Account, Link

# Set the route and accepted methods
@links.route("/", methods=['GET', 'POST'])
def account_index(account):
    return 'Account: %s' % (g.account_subdomain)

# Route for calls with an account subdomain and a link slug
@links.route("/<slug>", methods=['GET', 'POST'])
def get_link(account, slug):

    # TODO Retrieve the destination link in the database based on the slug

    return 'Slug: %s' % (slug)