from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Add another page
@app.route('/new_page')
def new_page():
    return 'This is another page!'

# on Windows:
#Export FLASK_APP=hello.py
#flask run


# Another way to run hello world 
# if you add this, you can run the flask app as: python hello.py

if __name__=="__main__":
    app.run(debug=True)