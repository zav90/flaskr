from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = r"mysql+pymysql://sql7245242:YzvNeHxF8X@sql7.freemysqlhosting.net:3306/sql7245242"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username="Zav9027",
    password="iliyaZav27",
    hostname="Zav9027.mysql.pythonanywhere-services.com",
    databasename="Zav9027$Gambling",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 100


db = SQLAlchemy(app)


class Example(db.Model):
    __tablename__ = 'Games'
    id = db.Column('id',db.Integer,primary_key=True)
    team1 = db.Column('team1',db.VARCHAR(length=100))
    team2 = db.Column('team2', db.VARCHAR(length=100))

    def __init__(self,id,team1,team2):
        self.id = id
        self.team1 = team1
        self.team2 = team2


@app.route('/')
def hello():
    games = Example.query.all()
    return render_template('index.html',games=games)


@app.route('/test')
def hello_world():
    string = 'roman is in the house'
    return 'Hello World! {} HEY HEY'.format(string)



if __name__ == '__main__':
    app.run(debug=True)
