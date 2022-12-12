from website import create_app # Import create app from website folder (now a python package)

app = create_app() # Create the app

if __name__ == '__main__' :
    app.run(debug=True) # Start the web server