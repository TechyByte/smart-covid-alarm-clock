# Begin logging before launching package
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(levelname)s - %(message)s')

# The Flask app is in a package to allow more efficient development
from app import app
