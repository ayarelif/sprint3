from flask import Flask,render_template, request
from .db_model import DB,User,Tweet
from .predict import predict_user
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
            if request.method=="post":
                add_user_tweepy(name)
                message="User {} successfully added!", format(name)
            tweets = User.query.filter(User.username==name).one().tweet 
        except Exception as e:
            print('Error addidng {}: {}'.format(name, e))
            tweets= []
        return render_template("user.html", title=name, message=message)

   
@app.route('/compare', methods=['POST'])
def compare(message=""):
    user1=request.values["user1"]
    useer2=request.values['user2']
    tweet_text=request.values['tweet_text']

    if user1== user2:
        message= "can not compare a user to themselves."
    else:
        prediction=predict_user(user1,user2,tweet_text)

        message= f'''{tweet_test} is more likely to be said by {user1 if prediction else user2}
                      than {user2 if prediction else user1}'''

    return render_template("predict.html",title="prediction",message=message)

 return app

#export FLASK_APP=twitoff:APP
#export FLASK_ENV=development
