# Creating Website Routes
from flask import Blueprint, render_template # Import Blueprint and render_template

views = Blueprint('views', __name__) # Define a Blueprint

# Make a decorator
@views.route('/') # Define the roots ('/')
def home(): # Home function
    return render_template("home.html", text="Hello,", user="Caleb") # Passing variables 