import os

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

'''
# Get the value of the DEBUG environment variable, otherwise set DEBUG to False by default
try:  
    # Only set DEBUG to True if explicitly set as True in environment
    if os.environ["DEBUG"] == "True":
        app.config["DEBUG"] = True
    else:
        app.config["DEBUG"] = False
except KeyError:
    # DEBUG config value not found, set to False by default
    print("DEBUG not set in environment; defaulting to False")
    app.config["DEBUG"] = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
'''

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
