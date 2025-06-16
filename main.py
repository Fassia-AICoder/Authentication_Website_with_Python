from website import create_app #import my funtion I have done in my file __init__.py

app = create_app() #called my function to use it

if __name__ == '__main__':
    app.run(debug=True) #permit to run flask application