from flask import Flask # Import Module Flask

def create_app() : # Membuat Aplikasi File
    app = Flask(__name__) # Nama File
    app.config['SECRET_KEY'] = 'ThyJoni17' # Secret Key
    
    # Register the blueprint
    from .views import views # Import views
    from .auth import auth # Import auth
    
    app.register_blueprint(views,url_prefix='/') # Accessing the url prefix for views
    app.register_blueprint(auth,url_prefix='/') # Accessing the url prefix for auth
    
    return app