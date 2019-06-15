# Package Imports
import os
import sys

# Add the project folder to the python checking path.
# This allows us to import files from anywhere in the project.
def Setup ():
    sys.path.append (os.path.dirname (os.path.abspath (__file__)))
