# Creating Website Authentication
from flask import Blueprint, render_template, request, flash # Import

auth = Blueprint('auth', __name__) # Define a Blueprint

# Login route
@auth.route('/login', methods=['GET', 'POST']) # Array of HTTP request
def login():
    return render_template("login.html")

# Logout route
@auth.route('/logout')
def logout():
    return "<h2>Logout</h2>"

# Signup route
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Get user data from post 
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4 :
            flash('Email must be greater than 3 characters.', category='error') # Message flashing
        elif len(firstName) < 2 :
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2 :
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7 :
            flash('Password must be at least 7 characters.', category='error')
        else :
            # add user to database
            flash('Account created!', category='success')
        
    return render_template("sign_up.html")
