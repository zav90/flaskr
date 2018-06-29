from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sshtunnel
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r"mysql+pymysql://sql7245242:YzvNeHxF8X@sql7.freemysqlhosting.net:3306/sql7245242"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = 'Games'
    id = db.Column('id',db.Integer,primary_key=True)
    team1 = db.Column('team1',db.VARCHAR)
    team2 = db.Column('team2', db.VARCHAR)

    def __init__(self,id,team1,team2):
        self.id = id
        self.team1 = team1
        self.team2 = team2

@app.route('/')
def hello():
    return '<h2>testing<h2>'


@app.route('/test')
def hello_world():
    string = 'roman is in the house'
    return 'Hello World! {} HEY HEY'.format(string)



if __name__ == '__main__':
    app.run()
