from flask import Flask # Import Module Flask
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() # Membuat database
DB_NAME = "database.db"

def create_app() : # Membuat Aplikasi File
    app = Flask(__name__) # Nama File
    app.config['SECRET_KEY'] = 'ThyJoni17' # Secret Key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # Database directory
    db.init_app(app)
        
    # Register the blueprint
    from .views import views # Import views
    from .auth import auth # Import auth
    
    app.register_blueprint(views,url_prefix='/') # Accessing the url prefix for views
    app.register_blueprint(auth,url_prefix='/') # Accessing the url prefix for auth
    
    from .models import User, Note # Import file models

    with app.app_context():
        db.create_all()
    
    # If the user hasn't login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' 
    login_manager.init_app(app)
    
    # Telling flask how to load the user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

# Mengecek database, kalau tidak ada membuat baru (OLDER VERSION OF FLASK SQLALCHEMY!)
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')