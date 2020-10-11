from flask import Flask,render_template, request
from .db_model import DB,User,Tweet


def create_app():
    """Create and condigure an instance of our flask applicaton"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Lambda School\\Unit3\\twitoff\\sprint3\\twitoff.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    #C://Lambda Schoo//Unit3//twitoff//sprint3
    DB.init_app(app) #connect Flask app to SQLAlchemy DB

    @app.route('/')
    def root():
        return render_template("base.html", title="home", users=User.query.all() )
    

    @app.route('/user', methods=["POST"])
    @app.route('/user/<name>', methods=["GET"])
    def add_or_update_user(name=None,message=""):
        name= name or request.values["user_name"]

        try:
            if request.method=="POST":
                add_user_tweepy(name)
                message="User {} successfully added!", format(name)
            tweets = User.query.filter(User.username==name).one().tweet 
        except Exception as e:
            print('Error addidng {}: {}'.format(name, e))
            tweets= []
        return render_template("user.html", title=name, message=message)

    return app
       

# Flask enviroment: export FLASK_APP=twitoff:APP and then flask run
#flask shell

#from twitoff.db_model import DB, User, Tweet
#DB
#DB.create_all()
# or add DB.drop_all()

